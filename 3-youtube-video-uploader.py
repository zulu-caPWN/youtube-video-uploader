from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import csv

banner = '###########################'

video_file_csv = ''
vid_title_csv = ''
vid_description_csv = ''
video_tag_text_csv = ''

with open('records.csv') as f:
    reader = csv.DictReader(f)
    csv_data = [r for r in reader]


binary = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
fp = webdriver.FirefoxProfile()
driver = webdriver.Firefox(firefox_binary=binary, firefox_profile=fp,
                           executable_path=r'C:\Users\PK\Desktop\VM_Shared_Folder\01Jan\upload_vid_youtube\geckodriver.exe')
wait = WebDriverWait(driver,20)
print 'Starting Browser'

######################
# EMAIL AND PASSWORD #
######################
email = '******************'
password = '******************'


for i in csv_data:
    if i['video_file_csv'] == '':
        continue
    else:
        print banner
        print i['video_file_csv']
        print i['vid_title_csv']
        print i['vid_description_csv']
        print i['video_tag_text_csv']



    #######################################
    # LOGIN TO GOOGLE / GO TO UPLOAD PAGE #
    #######################################
    sleep(2)
    driver.get('https://youtube.com/upload')
    sleep(1)

    if 'to continue to YouTube' in driver.page_source:
        print 'We have to sign in'
        email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        email_field.send_keys(email)
        print 'Email submitted'
        sleep(1)

        next_button = driver.find_element_by_xpath('//*[@id="identifierNext"]')
        next_button.click()
        sleep(3)

        pwd_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
        pwd_field.send_keys(password)
        print 'Password submitted'
        sleep(1)

        next_button = driver.find_element_by_xpath('//*[@id="passwordNext"]')
        next_button.click()
        print 'Logged In'


    else:
        print 'Already logged in'


    ###########################################
    # GO TO YAHOO AND COME BACK TO UPLOAD PAGE #
    ###########################################
    # sleep(2)
    # print 'Trying to evade Google'
    # driver.get('https://yahoo.com')
    # sleep(2)
    # driver.get('https://youtube.com/upload')



    ################
    # UPLOAD VIDEO #
    ################
    print 'Trying upload'
    sleep(1)
    upload_started = False
    try:
        defaults = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div[2]/div')
        if defaults.text == 'Did you know you can set defaults for future uploads?':
            print 'Found: Did you know you can set defaults for future uploads?'
            sleep(5)
            print 'Going to click it closed'
            click2 = driver.find_element_by_css_selector('button.yt-uix-close:nth-child(2)')
            sleep(2)
            click2.click()
            defaults = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[2]/div[2]/div')
            if defaults.text == 'Did you know you can set defaults for future uploads?':
                print 'It didnt work'
                sleep(300) #sleep while we figure out how to disable it
            else:
                print 'We successfully clicked it, now proceeding'
    except:
        print 'No cockblock Default text'
        pass
    while not upload_started:
        try:
            sleep(3)
            select_file_to_upload_input = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[4]/div[1]/div[1]/div[2]/input')
            sleep(1)
            select_file_to_upload_input.send_keys(i['video_file_csv'])
            upload_started = True
        except:
            print 'Couldn\'t upload'
            driver.refresh()



    ###############
    # VIDEO TITLE #
    ###############
    vid_title = driver.find_element_by_name('title')
    vid_title.clear()
    sleep(1)
    vid_title.send_keys(i['vid_title_csv'])
    sleep(1)
    print "Entered video title"


    #####################
    # VIDEO DESCRIPTION #
    #####################
    vid_description = driver.find_element_by_xpath('html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[1]/div/label[2]/span/textarea')
    vid_description.send_keys(i['vid_description_csv'])
    sleep(1)
    print 'Entered description'



    ##############
    # VIDEO TAGS #
    ##############
    sleep(3)
    vid_tags = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[1]/div/div/span/div/span/input')))
    vid_tags.send_keys(i['video_tag_text_csv'] + str(','))
    sleep(1)
    print 'Entered tags'


    ##################
    # OUR VIDEOS URL #
    ##################
    new_vid_link = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/a')))
    print 'Video url:', new_vid_link.text
    sleep(1)


    #########################
    # ADVANCED SETTINGS TAB #
    #########################
    sleep(2)
    advanced_settings_tab = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[1]/ul/li[3]/div[1]/a')))
    advanced_settings_tab.click()
    sleep(1)
    print 'Selected advanced settings tab'


    ###################
    # SELECT CATEGORY #
    ###################
    sleep(3)
    category_dropdown = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[4]/div/div[2]/label/div/ng-form[1]/span/select/option[14]')))
    category_dropdown.click()
    print 'Selected category: Science and Technology'
    sleep(1)


    ##################
    # Allow Comments #
    ##################
    allow_comments = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[4]/div/div[1]/div[1]/div[1]/div[1]/span/select/option[2]')))
    allow_comments.click()
    sleep(1)


    ##################
    # Basic Info Tab #
    ##################
    basic_info_tab = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[1]/ul/li[1]/div[1]/a')))
    basic_info_tab.click()
    sleep(1)


################This is where the "quality left sidebar notice" needs to be addressed #######################
####This will loop forever if quality issue, i need to check for quality and publish anyway after 5 loops
####Problem is that I cant seem to trigger a quality issue to program the bypass
    #################
    # Upload Status #
    #################
    sleep(2)
    upload_status = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[2]/div[2]/div[1]')))
    while upload_status.text != 'Upload complete!':
        print 'Still uploading & processing'
        sleep(5)
        upload_status = driver.find_element_by_xpath(
            '/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[2]/div[2]/div[1]')


    print 'Upload complete'
    thumb_status = False

    while not thumb_status:
        try:
            sleep(2)
            vid_thumbnail = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[2]/div/div/div[1]/div[3]/form/div[1]/fieldset[3]/div/span[2]/div[1]')
            vid_thumbnail.click()
            thumb_status = True
        except:
            print 'No thumbnail yet'
            sleep(5)
            thumb_status = False

    sleep(2)
    print 'Selected first thumbnail'


    #################
    # PUBLISH VIDEO #
    #################
    print 'Ready to publish'
    try:
        while publish_button.is_displayed():
            sleep(5)
            publish_button = driver.find_element_by_xpath(
                '/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/button/span')
            #sleep(2) #commenting (or maybe it's creating the publish_button var b4 trying to use it??) this out makes us enter the long except statement below, which happens to work.
            #uncommenting it would mean a successful first click publish but I would need to take the below except code and incorporate
            #it here. Nope.
            publish_button.click()
            print 'Video Published'
    except:
        print 'First publish attempt didn\'t work'
        count = 2
        good_upload = False
        while not good_upload:
            sleep(5)
            publish_button = driver.find_element_by_xpath(
                '/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/button/span')
            try:
                publish_button.click()
                sleep(5)
                try:
                    uploaded_title = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[3]')
                    sleep(1)
                    if uploaded_title.text == i['vid_title_csv']:
                        print 'Yes the titles match'
                        good_upload = True
                        sleep(2)
                        continue
                except:
                    print 'I couldnt match titles'
                    pass
                print 'Video Published'
            except:
                print 'Publish attempt', count, 'did not work either'
                count += 1
                if count == 5:
                    sleep(2)
                    """below is for when youtube pops in a notice saying our vid has quality issues"""
                    try:
                        audio_issues = driver.find_element_by_xpath('/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[2]/div[2]/div[3]/div/h3')
                        sleep(1)
                        if audio_issues:
                            #this may need to be the same as the regular publish button process right here
                            publish_button = driver.find_element_by_xpath(
                                '/html/body/div[2]/div[4]/div/div[5]/div/div[4]/div[2]/div/div[3]/div[1]/div[1]/div/div/button/span').click()

                    except:
                        print 'I dunno, didn\'t find any quality issues'

print 'Done'
