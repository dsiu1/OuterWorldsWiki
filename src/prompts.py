terminal_prompt = """Please help OCR the following images. These images represent a computer terminal in a video game, where 
    each note can be opened. 

    At the top of each terminal there is a title of the message starting with 

    FROM:
    TO:
    SUBJECT:

    Afterwards, there will be text for that message. However, since the text cannot fit the whole page in one screenshot,
    there will be many consecutive images. If you see a message that is cut off, please continue it in the next image. Please do not
    split it into multiple messages. For example avoid the following scenario output:

    ---
        
    The Grand Colonial Hotel
    =========================

    FROM: UNKNOWN_CLIENT
    TO: Bellamy, Ruth
    SUBJECT: SUBJECT_NOT_FOUND

    ====  
    DECRYPTION_ERROR  
    ...  
    MESSAGE CORRUPTED  
    ...  
    MEMORY CORRUPTED


    The Grand Colonial Hotel
    =========================

    SUBJECT: SUBJECT_NOT_FOUND

    ====  
    DECRYPTION_ERROR  
    ...  
    MESSAGE CORRUPTED  
    ...  
    MEMORY CORRUPTED  
    ...  
    DISPLAYING RECOVERED DATA  
    ...  
    
    knows the truth  
    please hurry  
    don't know how much longer I can keep this up

    ---

    Instead, only output the following:

    ---

    The Grand Colonial Hotel
    =========================
    FROM: UNKNOWN_CLIENT
    TO: Bellamy, Ruth
    SUBJECT: SUBJECT_NOT_FOUND

    ====  
    DECRYPTION_ERROR  
    ...  
    MESSAGE CORRUPTED  
    ...  
    MEMORY CORRUPTED  
    ...  
    DISPLAYING RECOVERED DATA  
    ...  
    
    knows the truth  
    please hurry  
    don't know how much longer I can keep this up

    ---

    For each new set of titles, please separate them with a new line. You do not need to include text near the bottom of the terminal
    where it may start with the number [1], [2], etc. 

    Please do not include any other text, just the text from the terminal. 


    """

log_prompt = """Please help OCR the following images. These images represent a computer terminal in a video game, where 
    each note can be opened. 

    At the top of each image there is a title

    Afterwards, there will be text for that message. However, since the text cannot fit the whole page in one screenshot,
    there will be many consecutive images. If you see a message that is cut off, please continue it in the next image. Please do not
    split it into multiple messages. For example avoid the following scenario output:

    ---
        
    The Grand Colonial Hotel
    =========================
    DECRYPTION_ERROR  
    ...  
    MESSAGE CORRUPTED  
    ...  
    MEMORY CORRUPTED


    The Grand Colonial Hotel
    =========================
    DECRYPTION_ERROR  
    ...  
    MESSAGE CORRUPTED  
    ...  
    MEMORY CORRUPTED  
    ...  
    DISPLAYING RECOVERED DATA  
    ...  
    
    knows the truth  
    please hurry  
    don't know how much longer I can keep this up

    ---

    Instead, only output the following:

    ---

    The Grand Colonial Hotel
    ========================

    DECRYPTION_ERROR  
    ...  
    MESSAGE CORRUPTED  
    ...  
    MEMORY CORRUPTED  
    ...  
    DISPLAYING RECOVERED DATA  
    ...  
    
    knows the truth  
    please hurry  
    don't know how much longer I can keep this up

    ---



    Please do not include any other text, just the text from the terminal. 
    """
