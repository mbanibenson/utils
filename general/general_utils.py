import numpy as np
import cv2 as cv
import urllib.request

'''

PLEASE ADD AN ENTRY HERE FOR EVERY UTIL ADDED FOR EASE OF REFERENCE
------------------------------------------------------------------------
1. download_video_from_url(url, output_name)
2. process_video_frames_and_show_outputs(video_file, processing_function, **kwargs)
3. 

'''

def download_video_from_url(url, output_name):
    '''
    Download the video file from remote url and store it with file name
    
    Arguments
    -----------
    url: str
        Link to remote video resource that you widh to download
        
    output_name: str
        Name of the video file after download, including the extension. Example 'video_name.mp4'
        
    Returns
    ----------
    video_file: Downloaded file is at the location specified by output_name
    
    
    
    Example:
    -----------
    
    download_video_from_url(url = 'https://dm0qx8t0i9gc9.cloudfront.net/watermarks/video/GTYSdDW/beautiful-nature-norway-natural-landscape-aerial-footage-lovatnet-lake_hcibgp7xg__57356fbaf561502638b61002438d8f1b__P360.mp4', 
                            output_name='street_video.mp4')
    
    '''
    try:
        print("Downloading starts...\n")
        
        temp = urllib.request.urlretrieve(url, output_name)
        
        print("Download completed..!!")
        
    except Exception as e:
        
        print(e)
        
        
def process_video_frames_and_show_outputs(video_file, processing_function, **kwargs):
    '''
    Given a video file, and a processing function, pass each frame to the processing function and show the results.
    
    Note: The processing function should take as input an RGB image as first argument (supply additional arguments as **kwargs) and return an image. Supply other function key word arguments as kwargs. See example below.
    
    Arguments
    -----------
    video_file: str
        path to the video file on disk, not remote.
        
    processing_function: function
        function to process a frame and return a frame
        
    **kwargs: additional key word arguments to supply to the function processing frames
    
    Returns:
    ------------
    visualization of the outputs of the function for every frame
    
    Example:
    -------------
    ##This is a toy processing function. Takes an image as input, alongside some arguments, and returns an image.##
    def fn(img, add, sub):
    
        out = img + add - sub

        return out
        
    ## Call the function as follows##
    process_video_frames_and_show_outputs('street_video.mp4', fn, add = 0.1, sub = 0.2)
    
    
    '''
    cap = cv.VideoCapture(video_file)
    
    while cap.isOpened():
        
        ret, frame = cap.read()
        
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        
        #Opencv loads images as bgr, so we convert to rgb
        input_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        #Get the output of the processing frame. Should be an image/frame
        output_frame = processing_function(input_frame, **kwargs)
        
        cv.imshow('frame', output_frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()
    