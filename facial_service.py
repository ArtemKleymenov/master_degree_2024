DATABASE = '../../_images/'
STREAM_URL = 'rtsp::/127.0.0.1:8500'
LAST_FRAME = None
THRESHOLD = 0.77

def run_fr_service():
    from deepface import DeepFace
    import cv2
    from collections import Counter


    cap = cv2.VideoCapture(STREAM_URL)
    if not cap.isOpened():
        exit(1)

    THRESHOLD = 15
    MAXIMA = (THRESHOLD + THRESHOLD//2)
    ans = [0] * MAXIMA
    n_frame = 0

    try:
        flag=True
        while cap.isOpened():
            ready, frame = cap.read()

            if not ready:
                continue

            snap = frame
            LAST_FRAME = frame.copy()
            try:
                dfs = DeepFace.find(img_path = snap, 
                        db_path = DATABASE, 
                        distance_metric = 'cosine',
                        enforce_detection=True,
                        detector_backend='yolov8', #yolov8
                        model_name='VGG-Face',     #ArcFace
                        silent=True,
                        normalization='ArcFace',
                        threshold=THRESHOLD
                )
                name = 0
                if dfs:
                    df=dfs[0]
                    line=df

                    if not line.empty:
                        name, x, y = line.identity.iloc[0],\
                                line.source_x.iloc[0],\
                                line.source_y.iloc[0]

                        name = name.split('/')[-1][:-4]

                        who, many = Counter(ans).most_common(1)[0]
                        if who != 0 and many > THRESHOLD:
                            snap=cv2.putText(snap.copy(), f'{who}', 
                                            (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, 
                                            (255, 20, 0), 2, cv2.LINE_AA)
                            if flag:
                                print(f'HELLO, {who}!')
                                flag = False
                        else: 
                            flag = True
                    
                        x2,y2 = line.source_w.iloc[0], line.source_h.iloc[0]
                        h,w=y+y2, x+x2
                        crop = snap[y:h, x:w]

                ans[n_frame] = name
                n_frame += 1
                n_frame %= MAXIMA
            except Exception as e: # TODO: error checker
                # print(e)
                continue
            finally:
                cv2.imshow('w', snap)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
    finally:
        cap.release()


if __name__ == '__main__':
    run_fr_service()
