# 배포!

### 배포 전 체크 리스트

- Django에서 예상되는 수준의 보안을 제공하도록 설정해야 합니다.
- 각 환경에 맞도록 설정해야 합니다.
- 선택적인 보안 기능들을 활성화시켜야 합니다.
- 성능 최적화가 적용돼야 합니다.
- 에러 보고가 제공되어야 합니다.

### 중요

##### SECRET_KEY
- 시크릿 키는 절대 유출하면 안 됨.
(현재는 settings.py로 넣어뒀는데, 따로 관리하게 됨.)
- Session, 암호화 서명 등에서 사용

##### DEBUG
- 소스 코드, 로컬 변수, 설정 등이 유출되기 때문에 **Debug = False**로 처리하는 것이 기본 (대외비)

##### DATABASE
- 개발환경의 데이터 베이스, 실제 데이터 베이스 등이 나눠져 있게 됨.
- 환경마다 데이터 베이스 변경도 모두 설정해줘야 함.
- ID, PW 등도 별도의 파일로 빼서 모두 관리해 줘야 함.

##### STATIC ROOT
- STATICFILES_DIRS 가 기본적으로 개발환경에서 사용됨 (정적 파일 관리)
- 하지만 운영 환경에서는 우리가 지정한 스태틱 폴더에 정리가 필요함 > 고로 방식 수정이 필요함

### AWS Amazon Web Serviece

##### REGION
- 서울로 지정
- 학교에서 사용했을 때는 도쿄 밖에 없어서 항상 도쿄로 썼었는데, 감회가 새로움

##### EC2 생성
- server 대여
- Ubuntu Linux 사용 // 프리티어
- 키 페어 설정
> 프라이빗 키 : Mac은 .pem, Window는 .ppk
- 인스턴스 : 가상 서버를 하나 대여 받았다. (서버용 컴퓨터를 구매하기에는 무리가 있기 때문)
- 오프라인으로 구매할 경우, 서버실 온도/습도 관리, 서버 관리 인력, 보안적인 부분도 고려해야 함.
> 개발 트렌드로 봤을 때 오픈 클라우드는 필수 (상황에 맞게)

##### Ubuntu
- 서버용 PC
- `sudo apt-get update` //최신 버전 패키지 목록 받아오기
- `sudo apt-get upgrade` //각 패키지의 종속성들을 모두 고려하여 실제 업데이트 하기.
- `sudo shutdown -r now` : 지금 서버 재실행하기
- `sudo apt-get -y __program__` : program 다운로드 하기
- `ll` : `ls -l`과 동일 // 권한, 소유자, 갱신일, 파일 이름까지 보기
- `cat __file_name__` : __file_name__ 내용 읽기
 - `pwd` : 현재 경로 보기


###### 계정
###### 절대 까먹으면 안 되니 어딘가에 꼭 기록해둘 것!
- `sudo` : 권리자 권한으로 실행
- `sudo passwd __ID__` : 계정 비밀번호 변경
- `su` : root로 계정 전환
- `exit` : 끝내기
- `clear` : 창 지우기
- `sudo locale-gen ko_KR.UTF-8` : 지역, 언어 설정
- `sudo dpkg-reconfigure tzdata`, `Asia/Seoul` : 시간대 설정


###### AWS 위에 서버를 설치한 후 Public IP를 사용해 접속하면 접속이 되어야 하는데, 처음에는 보안 설정을 먼저 진행해 줘야 함.

> 인바운드 규칙 : 들어오는 것들에 대한 방화벽
- `HTTP 80 port`에 대해 접근 권한을 풀어줘야 함.
- 데이터 베이스와 관련해서도 포트를 열어줘야 작동 가능

> 아웃바운드 규칙 : 나가는 것들에 대한 방화벽

##### vi 에디터
- `i`/`a`/`o`를 눌러서 편집 모드로 전환 (`a`가 커서위치 다음 부터 입력)
- `esc`로 명령모드로 전환
- :wq로 저장하고 종료


##### Python 설치
- 파이썬을 사용하기 위한 제반 프로그램 설치
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncu
rsesw5-dev \xz-utils tk-dev
```
- pyenv 설치 : python 버전 관리를 용이하게 하기 위한 프로그램
`git clone https://github.com/pyenv/pyenv.git ~/.pyenv`

- pyenv 환경 변수 설정 :
> `sudo vi .bashrc`를 눌러 vi 에디터로 진입
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
eval "$(pyenv init --path)"
fi
```
> 맨 아래에 위 내용을 추가하고, :wq를 눌러 저장하고 종료

##### github에 업로드한 내용 서버에서 구동하기.

- `ssh-keygen` : 나오는 것들은 엔터 눌러서 마무리.
- `cat .ssh/id_rsa.pub` : 키 값 읽기
- github.com/__repository__ > settings > Deploy keys > Add deploy key 에 위 내용 붙여넣기 (private repository일 경우 해당 서버에서 내용을 clone 해가는 것은 허용하는 내용)
- `git clone __your_repository__`
- `pyenv local __your_python__` : pyenv로 설치한 python을 여기서 사용 하겠다.
- `python -m venv venv` : 가상환경 설치
- `source venv/bin/activate` : 윈도우와는 다르게 venv/bin/activate를 실행시켜줘야 함.
- `pip install -r requirements.txt` pip freeze로 저장했던 requirements들을 한 번에 다운로드 함.