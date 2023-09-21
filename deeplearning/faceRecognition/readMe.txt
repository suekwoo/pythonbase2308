https://repo.anaconda.com/archive/

에서 Anaconda3-2023.07-2-Windows-x86_64.exe를 다운 받아 실행 하였습니다 

install 시에 크게 입력할 사항을 없습니다 

중간에 just me를 선택하시고 계속 다음을 선택하시면 됩니다 



1) webcam 준비 합니다
2) makeImage.py를 실행하고나면 동영상이 보입니다 
   동영상에 마우스를 클릭하고 소문자 'c'를 입력합니다 
   콘솔상에 'member name을 입력 하세요(영문) ' 메세지가 나오면 이미지 이름을 입력하세요 
3) 이미지를 켑쳐하여 얼굴만 보이게 작은 이미지로 만드세요
4) member folder에 넣으세요
5) anaconda prompt를 열어서 cmd창에 
   ﻿
   https://github.com/shashankx86/dlib_compiled/blob/v19.22/dlib-19.22.99-cp39-cp39-win_amd64.whl
   다운 받아 prompt 폴더에  넣습니다 
   
   
   conda install -e conda-forge dlib
   pip install face_recognition
   
   실행합니다
﻿
6) spyder는 종료후 재시작 합니다 
face_recognition.py를 실행하면 동영상이 뜨고 member 폴더안에 이미지의 이름을 보실수 있습니다


   