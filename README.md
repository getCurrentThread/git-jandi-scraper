# Git 잔디 스크래퍼 사용법 가이드

- 제작 : 김시영
- 수정 : 현진혁 (getCurrentThread)

## 폴더 구조

```
crawler
└── git_jandi_scrap.py
└── members.csv
└── secrets.json
└── README.md
```

`members.csv`, `secrets.json` 작성 후

`git_jandi_scrap.py` 실행하면 

`git_check_result.csv`에 결과가 저장됩니다.

## 주의할 점

gitlab 프로필을 공개로 하지 않아서 크롤링이 불가능한 경우가 발생하므로 검색하려는 프로필에 공개 설정을 필요로합니다.

## 패키지 설치

```shell
$pip install -r requirements.txt
```

### 정보 입력

- 필요한 코드 수정 목록
  ```python
  # 사이트 주소
  GITLAB_LOGIN_URL = f"https://<깃랩 로그인 주소 URL>" #해당 주석을 해제하고 작성 필요
  GITLAB_URL = f"https://<깃랩 주소 URL>/"
  ```

- 필요한 파일 목록

  ```
  1. secrets.json    --- 사용자 계정 정보
  2. members.csv     --- 이슈 스크래핑 대상자 명단
  ```

- **secrets.json**

```json
{
    "COACH_ID" : "",
    "COACH_PASSWORD" : ""
}
```

- **members.csv**

크롤링 할 gitlab 아이디 목록이 들어있는 csv파일

이 목록에 있는 순서대로 크롤링 합니다.

```
member0,홍길동
member1,나열한
member2,김이열
...
```

### 3. 결과물(예시)
- **git_check_result.csv**

각 gitlab 잔디에 찍힌 숫자를 나열한 파일 (엑셀이 편함)

```
(아이디), (커밋 수 ... ) 
member0, 0, 0, 0, 0, 0, 0 ...
member1, 0, 0, 0, 0, 0, 0 ...
```

제일 뒤에있는 숫자가 오늘 날짜에 찍힌 커밋 수 입니다.