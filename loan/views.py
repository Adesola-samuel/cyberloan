import cv2
from pyzbar import pyzbar
import pandas as pd
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import PredictionForm, CreateUserForm, UserLoginForm
from .models import Prediction, Help, Contributor
from django.contrib.auth.models import User
from sklearn.externals import joblib
from django.core.paginator import Paginator
from django.contrib import messages
from  django.conf import settings
from django.contrib.auth import authenticate, login, logout, load_backend
from django.contrib.auth.decorators import login_required
import pyttsx3

def audioread(statement):
    speaker = pyttsx3.init()
    speaker.say(statement)
    speaker.runAndWait()

lassoRegressor = joblib.load('./model/LassoRegressor.pkl')
logisticClassifier = joblib.load('./model/LogisticClassifier.pkl')

@login_required(login_url='loan:login')
def index(request):
    return render(request, "home.html", {})

@login_required(login_url='loan:login')
def prediction(request):
    context = {}
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            temp = {'Gender': form.cleaned_data['gender'],
                    'Married': form.cleaned_data['married'],
                    'Dependents': form.cleaned_data['dependents'],
                    'Education': form.cleaned_data['education'],
                    'Self_Employed': form.cleaned_data['self_employed'],
                    'ApplicantIncome': form.cleaned_data['applicant_income'],
                    'CoapplicantIncome': form.cleaned_data['coapplicant_income'],
                    'LoanAmount': form.cleaned_data['loan_amount'],
                    'Loan_Amount_Term': form.cleaned_data['loan_amount_term'],
                    'Credit_History': form.cleaned_data['credit_history'],
                    'Property_Area': form.cleaned_data['credit_history']}

            temp2 = temp.copy()
            del (temp2['LoanAmount'])
            context['name'] = request.POST.get('name')

            testdata = pd.DataFrame(temp, index=[0])
            testdata2 = pd.DataFrame(temp2,index=[0])

            status = logisticClassifier.predict(testdata)
            status= status[0]
            print(temp)
            print('LOAN STATUS = ',status)
            temp['name'] = request.POST.get('name')

            if status == 0.0:
                statement='Congratulations!',temp['name'], '. You applied for a loan of', temp['LoanAmount'], 'naira only. Your loan will be approved. Thanks for trusting Smart Cyber-Loan.'
                audioread(statement)
                context['positive_status'] = 'Congrats!, your loan will be approved.'
                loan_status = 'Loan Approved'
                temp['Loan_Status'] = 'Approved'
                context['form'] = form
                #form.save()
            elif status == 1.0:
                recommendedAmount = lassoRegressor.predict(testdata2)[0]
                if recommendedAmount >= 0:
                    if recommendedAmount > int(temp['LoanAmount']):
                        context['recommendedAmount'] = recommendedAmount
                        temp['Loan_Status'] = 'Approved'
                        statement='Congratulations!', temp['name'], '. You applied for a loan of', temp['LoanAmount'],'naira only. Your loan will be approved. Actually, you can borrow as much as ',recommendedAmount,' naira only. Thanks for trusting Smart Cyber-Loan.'
                        audioread(statement)
                        context['probation_status'] = recommendedAmount
                    else:
                        statement='Sorry!',temp['name'], '. You applied for a loan of ', temp['LoanAmount'], 'naira only.', 'Your loan may not be approved, your credit limit may be too low! your loan may be approved if you reduce your loan amount.'
                        audioread(statement)
                        context['consolidation_msg'] = 'Sorry! your loan may not be approved, reduce your loan amount and try again.'
                        temp['Loan_Status'] = 'Not Approved'
                else:
                    audioread('Sorry!, you are not be eligible for this loan!')
                    context['consolidation_msg'] = 'Sorry! are not eligible for this loan!'
                    temp['Loan_Status'] = 'Not Approved'
            context['form'] = form
            q = Prediction(
                name = temp['name'],
                gender=temp['Gender'],
                married=temp['Married'],
                dependents=temp['Dependents'],
                education=temp['Education'],
                self_employed=temp['Self_Employed'],
                applicant_income=temp['ApplicantIncome'],
                coapplicant_income=temp['CoapplicantIncome'],
                loan_amount_term=temp['Loan_Amount_Term'],
                credit_history=temp['Credit_History'],
                property_area=temp['Property_Area'],
                loan_amount=temp['LoanAmount'],
                loan_status=temp['Loan_Status'],
                user=request.user
            )
            q.save()
            return render(request, "prediction.html", context)

        else:
            context['form'] = form
            context['error_display'] = 'You entered invalid input, please fill the form properly!'
        return render(request, "prediction.html", context)
    else:
        context['form'] = PredictionForm()
        return render(request, "prediction.html", context)

def about(request):
    contributors = Contributor.objects.all()
    return render(request, "about.html", {'contributors':contributors,})

def terms_policy(request):
    return render(request, "terms_policy.html", {})

@login_required(login_url='loan:login')
def successful_predictions(request):
    current_user = request.user.id
    predictions = Prediction.objects.filter(user=current_user)
    paginator = Paginator(predictions, 10)
    page = request.GET.get('page')
    predictions = paginator.get_page(page)
    return render(request, "successful_predictions.html", {'predictions':predictions,})

@login_required(login_url='loan:login')
def help(request):
    if request.method=='GET':
        context={}
        query = request.GET.get('q','')
        if query:
            queryset = (Q(task__icontains=query) | Q(howto__icontains=query))
            results = Help.objects.filter(queryset).distinct()
            if results.count() == 0:
                context['no_result'] = 'No result match for this search.'
                return render(request, 'help.html', context)
            else:
                paginator = Paginator(results, 5)
                page = request.GET.get('page')
                results = paginator.get_page(page)
                context['results']= results
                return render(request, 'help.html', context)
        else:
            results = []
            context['results'] = results
            return render(request, 'help.html', context)
    return render(request, 'help.html')

@login_required(login_url='loan:login')
def help_detail(request,pk):
    context = {}
    context['result'] = Help.objects.get(pk=pk)
    return render(request, "help_detail.html", context)

def create_user(request):
    if request.user.is_authenticated:
        return redirect('loan:home')
    else:
        context = {}
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account Successfully created for ' + user )
                return redirect('loan:login')
        else:
            form = CreateUserForm()
        context['form'] = form
        return render(request, "create_user.html", context)

def login_page(request):
    audioread('Welcome to smart cyber-loan, enter your username and password to login')
    if request.user.is_authenticated:
        return redirect('loan:home')
    else:
        if request.method == 'POST':
            form = UserLoginForm(request.POST)
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('loan:home')
            else:
                context = {}
                context['form'] = UserLoginForm()
                messages.info(request, 'username or password is incorrect')
                return render(request, "login.html", context)

        context = {}
        context['form']=UserLoginForm()
        return render(request, "login.html", context)

def logout_user(request):
    logout(request,)
    return redirect('loan:login')

def qr_auth(request):
    statement = 'Please kindly navigate windows to camera about to open, present the back view of your I.D. card before camera. As soon as your card is detected, please press the Q button.'
    audioread(statement)
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_PLAIN

    while True:
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            App_id = obj.data
            cv2.putText(frame, str("QR DETECTED!"), (50, 50), font, 3,
                        (255, 0, 0), 3)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

    try:
        app_id = str(App_id);
        app_id = app_id[2];
        pk = int(app_id);
    except UnboundLocalError:
        return redirect('loan:login')

    check = User.objects.filter(id=pk)
    context = {}
    context['auth_page'] = 'auth page'
    if check.count() == 0:
        context['App_fail'] = "User does not exist!"
        return redirect('loan:login')
    else:
        user = User.objects.get(pk=pk)
        if not hasattr(user, 'backend'):
            for backend in settings.AUTHENTICATION_BACKENDS:
                if user == load_backend(backend).get_user(user.pk):
                    user.backend = backend
                    break
        if hasattr(user, 'backend'):
            login(request, user)
            statement = 'Welldone!',user.username,'. You have successfully logged in.'
            audioread(statement)
    return redirect('loan:login')

