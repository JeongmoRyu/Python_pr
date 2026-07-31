# 📌 문제: API 게이트웨이 동적 라우팅 및 로드 밸런싱
당신은 MSA(Microservice Architecture)로 구성된 컨테이너 환경의 트래픽을 제어하는 API 게이트웨이를 개발하고 있습니다. 게이트웨이는 들어오는 API URL을 분석하여 알맞은 백엔드 서비스로 요청을 전달(Routing)하고, 해당 서비스에 여러 대의 컨테이너가 띄워져 있다면 부하를 고르게 분산(Round-Robin)해야 합니다.
라우팅 규칙이 담긴 배열 routes와 클라이언트의 API 요청 URL이 담긴 배열 requests가 주어질 때, 각 요청이 어떤 컨테이너로 전달되었는지를 순서대로 배열에 담아 반환하는 함수를 완성하세요.

## 🌐 라우팅 및 로드 밸런싱 규칙
- routes의 요소는 "URL접두사 서비스명 컨테이너수" 형태의 문자열입니다. (예: "/api/users user_svc 3")
- 최장 접두사 매칭 (Longest Prefix Match):
  - 요청된 URL이 여러 개의 라우팅 규칙 접두사와 일치할 경우, 가장 길이가 긴 접두사를 가진 규칙을 따릅니다.
  - 일치하는 접두사가 단 하나도 없다면 "404"를 반환합니다.
- 라운드 로빈 (Round-Robin) 분산:
  - 서비스에 할당된 컨테이너 수가 $N$개일 때, 컨테이너 이름은 "{서비스명}-1" 부터 "{서비스명}-N" 까지 존재합니다.
  - 특정 서비스로 향하는 요청은 1번 컨테이너부터 순차적으로 전달되며, $N$번을 넘어가면 다시 1번으로 돌아옵니다.
  - 예: user_svc가 2대일 때, 요청이 들어올 때마다 user_svc-1 $\rightarrow$ user_svc-2 $\rightarrow$ user_svc-1 순으로 전달됩니다.
  
## 제한사항
- routes의 길이는 1 이상 1,000 이하입니다.
- requests의 길이는 1 이상 100,000 이하입니다.
- 컨테이너 수는 1 이상 10 이하의 자연수입니다.
- URL과 서비스명은 알파벳 소문자, 숫자, 슬래시(/), 하이픈(-)으로만 이루어져 있습니다.

## 입출력 예시

| routes | requests | result |
|---|---|---|
| `["/api/v1/auth auth_svc 2", "/api/v1/auth/admin admin_svc 1", "/api/v2 legacy 3"]` | `["/api/v1/auth/login", "/api/v1/auth/logout", "/api/v1/auth/admin/settings", "/api/v3/info", "/api/v1/auth/profile"]` | `["auth_svc-1", "auth_svc-2", "admin_svc-1", "404", "auth_svc-1"]` |
| `["/ route 1", "/img image 2"]` | `["/img/logo.png", "/index.html", "/img/bg.png"]` | `["image-1", "route-1", "image-2"]` |


#### 예시 1번 설명:
- "/api/v1/auth/login": "/api/v1/auth"와 일치 $\rightarrow$ auth_svc 첫 호출 (auth_svc-1)
- "/api/v1/auth/logout": "/api/v1/auth"와 일치 $\rightarrow$ auth_svc 두 번째 호출 (auth_svc-2)
- "/api/v1/auth/admin/settings": "/api/v1/auth"와 "/api/v1/auth/admin" 모두 일치하지만, 가장 긴 "/api/v1/auth/admin" 규칙 적용 $\rightarrow$ admin_svc 첫 호출 (admin_svc-1)
- "/api/v3/info": 일치하는 접두사 없음 $\rightarrow$ "404"
- "/api/v1/auth/profile": "/api/v1/auth"와 일치 $\rightarrow$ auth_svc 세 번째 호출이므로 다시 1번으로 회귀 (auth_svc-1)