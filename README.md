# Body_Balance_Evaluation_BE
first make base structure.
Use Python 3.11.9

```
/* python 3.11로 venv 생성 */
py -3.11 -m venv .venv
/* 생성된 venv 기준으로 활성화 */
.\.venv\Scripts\Activate.ps1
/* 필요시 pip 업그레이드 */
python -m pip install --upgrade pip
/* requirements에 저장해둔 라이브러리 설치 */
pip install -r requirements.txt
/* 만약 실행 안되고 mediapipe 관련 오류 뜰 경우 버전 확인하기 print(md) */
uvicorn main:app --reload
/* 세팅 설정 */
setting에 지정해둬서 ignore에 걸려서 안 올라갔으니 당연히 뜸[정상]
```
