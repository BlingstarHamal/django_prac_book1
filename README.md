# DJANGO 연습

## 이한영의 DJANGO 입문 (https://books.django.ac/) 을 보며 공부한 내용 중 나의 생각과 실수 등을 기록 합니다.


위 책의 pystagram 예제입니다.

~~1. 현재 include 오류를 겪고 있어서 수정 중~~
![Alt text](/read_images/image-1.png)
![Alt text](/read_images/image.png)

feeds.html 파일에서 내실수인듯 한데, '#post-'|concat:post_id -> 이부분에서 post.id로 해야했음.

p318 add 사용시
![Alt text](/read_images/p318.jpeg)

p320 concat 사용시
![Alt text](/read_images/p320.jpeg)

add 구문에선 post_id로 되는데, concat으로 바뀌었을 땐 동작하지 않는듯 함.
이 내용이 p320에도 반복되는데 해당 페이지에는 정상적으로 나와있는걸로 보아 add와 concat에서 차이가 있는것 같다.

2. 확장 프로그램 문제

prettier 등의 code formatter의 세이브 시 자동 수정 기능 조심
 나의 경우엔 "editor.formatOnSave": true 부분이 문제 였는데,
 장고 포맷을 제대로 지원하지 않아서 저장하면서 수정된 부분 때문에 코드가 제대로 돌아가지 않았다.

또한 자동 import 삽입 기능도 문제를 일으켰음!

---

### 완성된 샘플 페이지들

![Alt text](/read_images/image-2.png)
![Alt text](/read_images/image-3.png)
![Alt text](/read_images/image-4.png)
![Alt text](/read_images/image-5.png)
![Alt text](/read_images/image-6.png)
![Alt text](/read_images/image-7.png)


---
### 추가 진행사항

책에 나온 것에서 aws 업로드 전까지는 완료한 상황입니다.
1. css를 bootstrap으로 변경
2. summernote 적용 (post_add)
3. 페이지 접근 방법 수정 ( 로그인 없이 피드 읽기 가능 )
4. ajax 적용하는 중 -> 좋아요, 댓글 달았을때 새로고침 없이 하는게 목표
---
