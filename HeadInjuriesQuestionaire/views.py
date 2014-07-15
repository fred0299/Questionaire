from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from models import CoverSheet, Encounter, NonBlastHeadInjury
from datetime import datetime
#from django.utils import timezone
from HeadInjuriesQuestionaire.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def patientInformation(request):    
     
    inputSubjectID = request.POST["subjectID"]
    inputDate = request.POST["dateOfQuestionaire"]
    inputAdministrationNumber = request.POST["administrationNumber"]

    username = None

    if (request.user.is_authenticated()):
        username = request.user.username

    if request.method == 'POST':

        e = Encounter()

        e.subjectID = inputSubjectID
        e.dateOfQuestionaire = inputDate
        e.administrationNumber = inputAdministrationNumber
        e.createdBy = username
        e.dateCreated = datetime.now()

        e.save()

    return HttpResponseRedirect(reverse('HeadInjuriesQuestionaire:coverSheet', args=(e.id,)))

@login_required
def coversheetsubmit(request, e_id):
  
    # Question 1, 1a
    if (request.POST["rdQuestion1"] == 'rdAnswer1Yes'):
        question1 = 'Yes'
        question1a = int(request.POST["numAnswer1a"])
    else:
        question1 = 'No'
        question1a = None

    # Question 2, 2a, 2b, 2c
    if (request.POST["rdQuestion2"] == 'rdAnswer2Yes'):
        question2 = 'Yes'
        question2a = request.POST["numAnswer2a"]
        question2b = request.POST["numAnswer2b"] + ' ' + request.POST["ddAnswer2b"]
        question2c = request.POST["numAnswer2c"] + ' ' + request.POST["ddAnswer2c"]
    else:
        question2 = 'No'
        question2a = None
        question2b = None
        question2c = None

    # Question 3, 4, 4a, 4b, 5
    if (request.POST["rdQuestion3"] == 'rdQuestion3Yes'):
        question3 = 'Yes'
        question4 = int(request.POST["numAnswer4"])
        question5 = request.POST["numAnswer5"] + ' ' + request.POST["ddAnswer5"]
        if (int(request.POST["numAnswer4"]) > 10):
            question4a = request.POST["numAnswer4a"] + ' times per ' + request.POST["ddAnswer4a"]
            question4b = request.POST["numAnswer4b"] + ' ' + request.POST["ddAnswer4b"]
        else:
            question4a = None
            question4b = None
    else:
        question3 = 'No'
        question4 = None
        question4a = None
        question4b = None
        question5 = None

    # Question 6
    if (question1 == 'Yes' or question2 == 'Yes' or question3 == 'Yes'):
        
        if (request.POST.get("ckNoSymptoms") == 'on'):
            memoryProblems =        None
            balanceProblems =       None
            dizziness =             None
            sensitivityToLight =    None
            sensitivityToNoise =    None
            ringingInTheEars =      None
            irritability =          None
            headaches =             None
            sleepProblems =         None
            disorientation =        None
            troubleTrackingConv =   None
            lossOfHearing =         None
            vomitingOrNausea =      None
            changeInVision =        None
            otherSymptoms =         None
            NoSymptoms =            None
        else:

            if (request.POST.get("ckMemoryProblems") == 'on'):
                memoryProblems = 'Yes'
            else:
                memoryProblems = 'No'

            if (request.POST.get("ckBalanceProblems") == 'on'):
                balanceProblems = 'Yes'
            else:
                balanceProblems = 'No'

            if (request.POST.get("ckDizziness") == 'on'):
                dizziness = 'Yes'
            else:
                dizziness = 'No'

            if (request.POST.get("ckSensitivityToLight") == 'on'):
                sensitivityToLight = 'Yes'
            else:
                sensitivityToLight = 'No'

            if (request.POST.get("ckSensitivityToNoise") == 'on'):
                sensitivityToNoise = 'Yes'
            else:
                sensitivityToNoise = 'No'

            if (request.POST.get("ckRingingInTheEars") == 'on'):
                ringingInTheEars = 'Yes'
            else:
                ringingInTheEars = 'No'

            if (request.POST.get("ckIrritability") == 'on'):
                irritability = 'Yes'
            else:
                irritability = 'No'

            if (request.POST.get("ckHeadaches") == 'on'):
                headaches = 'Yes'
            else:
                headaches = 'No'

            if (request.POST.get("ckSleepProblems") == 'on'):
                sleepProblems = 'Yes'
            else:
                sleepProblems = 'No'

            if (request.POST.get("ckDisorientation") == 'on'):
                disorientation = 'Yes'
            else:
                disorientation = 'No'

            if (request.POST.get("ckTroubleTrackingConversations") == 'on'):
                troubleTrackingConv = 'Yes'
            else:
                troubleTrackingConv = 'No'

            if (request.POST.get("ckLossOfHearing") == 'on'):
                lossOfHearing = 'Yes'
            else:
                lossOfHearing = 'No'

            if (request.POST.get("ckVomiting") == 'on'):
                vomitingOrNausea = 'Yes'
            else:
                vomitingOrNausea = 'No'

            if (request.POST.get("ckChangeInVision") == 'on'):
                changeInVision = 'Yes'
            else:
                changeInVision = 'No'

            if (request.POST.get("ckNoSymptoms") == 'on'):
                NoSymptoms = 'Yes'
            else:
                NoSymptoms = 'No'

            if (NoSymptoms == 0):
                otherSymptoms = request.POST.get("txtOtherSymptoms")
            else:
                otherSymptoms = None

    else:
        memoryProblems =        None
        balanceProblems =       None
        dizziness =             None
        sensitivityToLight =    None
        sensitivityToNoise =    None
        ringingInTheEars =      None
        irritability =          None
        headaches =             None
        sleepProblems =         None
        disorientation =        None
        troubleTrackingConv =   None
        lossOfHearing =         None
        vomitingOrNausea =      None
        changeInVision =        None
        otherSymptoms =         None
        NoSymptoms =            None


    cs = CoverSheet()

    cs.encounter_id =           e_id
    cs.question1 =              question1
    cs.question1a =             question1a
    cs.question2 =              question2
    cs.question2a =             question2a
    cs.question2b =             question2b
    cs.question2c =             question2c
    cs.question3 =              question3
    cs.question4 =              question4
    cs.question4a =             question4a
    cs.question4b =             question4b
    cs.question5 =              question5
    cs.memoryProblems =         memoryProblems
    cs.balanceProblems =        balanceProblems
    cs.dizziness  =             dizziness
    cs.sensitivityToLight =     sensitivityToLight
    cs.sensitivityToNoise =     sensitivityToNoise
    cs.ringingInTheEars =       ringingInTheEars
    cs.irritability =           irritability
    cs.headaches =              headaches
    cs.sleepProblems =          sleepProblems
    cs.disorientation =         disorientation
    cs.troubleTrackingConv =    troubleTrackingConv
    cs.lossOfHearing =          lossOfHearing
    cs.vomitingOrNausea =       vomitingOrNausea
    cs.changeInVision =         changeInVision
    cs.otherSymptoms =          otherSymptoms
    cs.NoSymptoms =             NoSymptoms
    cs.save()

    return HttpResponseRedirect(reverse('HeadInjuriesQuestionaire:NonBlastHeadInjury', args=(e_id,)))

@login_required
def nonBlastHeadInjuryPage1(request, e_id):

    # Summary at top of screen
    eventDetailSummary = request.POST.get('txtEventDetailSummary')

    # Questions 1, 2, 3
    eventDetailQuestion1 = request.POST.get('eventDetailQuestion1')
    eventDetailQuestion2 = request.POST.get('txtEventDetailQuestion2')
    if (request.POST.get('ddEventDetailQuestion3') == 'default'):
        eventDetailQuestion3 = None
    else:
        eventDetailQuestion3 = request.POST.get('ddEventDetailQuestion3')

    # Questions 4, 4a
    if (request.POST.get('ddEventDetailQuestion4') == 'default'):
        eventDetailQuestion4 = None
        eventDetailQuestion4a = None
    elif(request.POST.get('ddEventDetailQuestion4') == 'yes'):
        eventDetailQuestion4 = request.POST.get('ddEventDetailQuestion4')
        eventDetailQuestion4a = None
    else:
        eventDetailQuestion4 = 'no'
        if (request.POST.get('ddEventDetailQuestion4a') == 'default'):
            eventDetailQuestion4a = None
        else:
            eventDetailQuestion4a = request.POST.get('ddEventDetailQuestion4a')

    # Questions 5, 5a
    if (request.POST.get('ddEventDetailQuestion5') == 'default'):
        eventDetailQuestion5 = None
        eventDetailQuestion5a = None
    elif(request.POST.get('ddEventDetailQuestion5') == 'no'):
        eventDetailQuestion5 = request.POST.get('ddEventDetailQuestion5')
        eventDetailQuestion5a = None
    else:
        eventDetailQuestion5 = 'yes'
        if (request.POST.get('ddEventDetailQuestion5a') == 'default'):
            eventDetailQuestion5a = None
        else:
            eventDetailQuestion5a = request.POST.get('ddEventDetailQuestion5a')

    # Questions 6, 6a
    if (request.POST.get('ddEventDetailQuestion6') == 'default'):
        eventDetailQuestion6 = None
        eventDetailQuestion6a = None
    elif(request.POST.get('ddEventDetailQuestion6') == 'no'):
        eventDetailQuestion6 = request.POST.get('ddEventDetailQuestion6')
        eventDetailQuestion6a = None
    else:
        eventDetailQuestion6 = 'yes'
        eventDetailQuestion6a = request.POST.get('txtEventDetailQuestion6a')

    # Questions 7, 7a
    if (request.POST.get('ddEventDetailQuestion7') == 'default'):
        eventDetailQuestion7 = None
        eventDetailQuestion7a = None
    elif(request.POST.get('ddEventDetailQuestion7') == 'no'):
        eventDetailQuestion7 = request.POST.get('ddEventDetailQuestion7')
        eventDetailQuestion7a = None
    else:
        eventDetailQuestion7 = 'yes'
        eventDetailQuestion7a = request.POST.get('txtEventDetailQuestion7a')

    # Questions 8, 8a
    if (request.POST.get('ddEventDetailQuestion8') == 'default'):
        eventDetailQuestion8 = None
        eventDetailQuestion8a = None
    elif(request.POST.get('ddEventDetailQuestion8') == 'no'):
        eventDetailQuestion8 = request.POST.get('ddEventDetailQuestion8')
        eventDetailQuestion8a = None
    else:
        eventDetailQuestion8 = 'yes'
        eventDetailQuestion8a = request.POST.get('txtEventDetailQuestion8a')

    # Question 9
    if (request.POST.get('ddEventDetailQuestion9') == 'default'):
        eventDetailQuestion9 = None
    else:
        eventDetailQuestion9  = request.POST.get('txtEventDetailQuestion9') + ' ' + request.POST.get('ddEventDetailQuestion9')

    # Question 10
    if (request.POST.get('ddEventDetailQuestion10') == 'default'):
        eventDetailQuestion10 = None
        eventDetailQuestion10a = None
    elif(request.POST.get('ddEventDetailQuestion10') == 'no'):
        eventDetailQuestion10 = request.POST.get('ddEventDetailQuestion10')
        eventDetailQuestion10a = None
    else:
        eventDetailQuestion10 = 'yes'
        eventDetailQuestion10a = request.POST.get('ddEventDetailQuestion10a')

    # Question 11, 11a, 11b
    if (request.POST.get('ddEventDetailQuestion11') == 'default'):
        eventDetailQuestion11 = None
        eventDetailQuestion11a = None
        eventDetailQuestion11b = None
    elif(request.POST.get('ddEventDetailQuestion11') == 'no'):
        eventDetailQuestion11 = request.POST.get('ddEventDetailQuestion11')
        eventDetailQuestion11a = None
        eventDetailQuestion11b = None
    else:
        eventDetailQuestion11 = 'yes'
        if (request.POST.get('ddEventDetailQuestion11a') == 'default'):
            eventDetailQuestion11a = None
            eventDetailQuestion11b = None
        elif (request.POST.get('ddEventDetailQuestion11a') == 'other'): # other is selected for 11a, so 11b is visible
            eventDetailQuestion11a = request.POST.get('ddEventDetailQuestion11a')
            eventDetailQuestion11b = request.POST.get('txtEventDetailQuestion11b')
        else: # quesiton 11a does not have default or other selected
            eventDetailQuestion11a = request.POST.get('ddEventDetailQuestion11a')
            eventDetailQuestion11b = None

    nbhi = NonBlastHeadInjury()

    nbhi.encounter_id =                 e_id
    nbhi.eventDetailSummary =           eventDetailSummary
    nbhi.eventDetailQuestion1 =         eventDetailQuestion1
    nbhi.eventDetailQuestion2 =         eventDetailQuestion2
    nbhi.eventDetailQuestion3 =         eventDetailQuestion3
    nbhi.eventDetailQuestion4 =         eventDetailQuestion4
    nbhi.eventDetailQuestion4a =        eventDetailQuestion4a
    nbhi.eventDetailQuestion5 =         eventDetailQuestion5
    nbhi.eventDetailQuestion5a =        eventDetailQuestion5a
    nbhi.eventDetailQuestion6 =         eventDetailQuestion6
    nbhi.eventDetailQuestion6a =        eventDetailQuestion6a
    nbhi.eventDetailQuestion7 =         eventDetailQuestion7
    nbhi.eventDetailQuestion7a =        eventDetailQuestion7a
    nbhi.eventDetailQuestion8 =         eventDetailQuestion8
    nbhi.eventDetailQuestion8a =        eventDetailQuestion8a
    nbhi.eventDetailQuestion9 =         eventDetailQuestion9
    nbhi.eventDetailQuestion10 =        eventDetailQuestion10
    nbhi.eventDetailQuestion10a =       eventDetailQuestion10a
    nbhi.eventDetailQuestion11 =        eventDetailQuestion11
    nbhi.eventDetailQuestion11a =       eventDetailQuestion11a
    nbhi.eventDetailQuestion11b =       eventDetailQuestion11b

    nbhi.save()

    return HttpResponseRedirect(reverse('HeadInjuriesQuestionaire:NonBlastHeadInjury2', args=(nbhi.id,)))

def nonBlastHeadInjuryPage2(request, nbhi_id):

    # Question 1
    if (request.POST.get('ddMemoryQuestion1') == 'default'):
        memoryQuestion1 = None
    else:
        memoryQuestion1 = request.POST.get('ddMemoryQuestion1')

    # Question 2, 2a, 2b
    if (request.POST.get('ddMemoryQuestion2') == 'default'):
        memoryQuestion2 = None
        memoryQuestion2a = None
        memoryQuestion2b = None
    elif (request.POST.get('ddMemoryQuestion2') == 'no'):
        memoryQuestion2 = request.POST.get('ddMemoryQuestion2')
        memoryQuestion2a = None
        memoryQuestion2b = None
    else:
        memoryQuestion2 = request.POST.get('ddMemoryQuestion2')
        memoryQuestion2a = request.POST.get('txtMemoryQuestion2a')
        memoryQuestion2b = request.POST.get('txtMemoryQuestion2b') + ' ' + request.POST.get('ddMemoryQuestion2b')

     # Question 3, 3a, 3b
    if (request.POST.get('ddMemoryQuestion3') == 'default'):
        memoryQuestion3 = None
        memoryQuestion3a = None
        memoryQuestion3b = None
    elif (request.POST.get('ddMemoryQuestion3') == 'no'):
        memoryQuestion3 = request.POST.get('ddMemoryQuestion3')
        memoryQuestion3a = None
        memoryQuestion3b = None
    else:
        memoryQuestion3 = request.POST.get('ddMemoryQuestion3')
        memoryQuestion3a = request.POST.get('txtMemoryQuestion3a')
        memoryQuestion3b = request.POST.get('txtMemoryQuestion3b') + ' ' + request.POST.get('ddMemoryQuestion3b')

    # Question 4
    if ((request.POST.get('ddMemoryQuestion1') == 'yes') and (request.POST.get('ddMemoryQuestion2') == 'no') and (request.POST.get('ddMemoryQuestion3') == 'no')):
        memoryQuestion4 = request.POST.get('ddMemoryQuestion4')
    else:
        memoryQuestion4 = None
    
    try:
        obj = NonBlastHeadInjury.objects.get(id = int(nbhi_id))
        obj.memoryQuestion1 = memoryQuestion1
        obj.memoryQuestion2 = memoryQuestion2
        obj.memoryQuestion2a = memoryQuestion2a
        obj.memoryQuestion2b = memoryQuestion2b
        obj.memoryQuestion3 = memoryQuestion3
        obj.memoryQuestion3a = memoryQuestion3a
        obj.memoryQuestion3b = memoryQuestion3b
        obj.memoryQuestion4 = memoryQuestion4
        obj.save()
    except NonBlastHeadInjury.DoesNotExist:
        return HttpResponse('Fail')

    return HttpResponseRedirect(reverse('HeadInjuriesQuestionaire:NonBlastHeadInjury3', args=(nbhi_id,)))

def nonBlastHeadInjuryPage3(request, nbhi_id):

    # Question 1
    if (request.POST.get('ddMemoryQuestion1') == 'default'):
        consciousnessQuestion1 = None
    elif (request.POST.get('ddMemoryQuestion1') == 'no'):
        pass
    else:
        consciousnessQuestion1 = request.POST.get('ddConsciousnessQuestion1')

    try:
        obj = NonBlastHeadInjury.objects.get(id = int(nbhi_id))
        obj.consciousnessQuestion1 = consciousnessQuestion1
        obj.save()
    except NonBlastHeadInjury.DoesNotExist:
        return HttpResponse('Fail')

    return HttpResponse('test')

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'HeadInjuriesQuestionaire/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/subject/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('HeadInjuriesQuestionaire/login.html', {}, context) 

def restricted(request):
    return HttpResponse("You are logged in.")

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/login')