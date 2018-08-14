Uploads videos to Youtube

It uses Python and Selenium to control a Firefox browser. The script imports a csv file located in the same dir by the name of records.csv
the headers of that csv need to include;

1. video_file_csv
 -> this is the complete path to where the video file lives on your HD

2. vid_title_csv
-> this will be the title of the uploaded video

3. vid_description_csv
-> this will be the description of the uploaded video

4. video_tag_text_csv
-> these will be the tags entered for the uploaded video, each tag (except the last one) must have a comma after it
