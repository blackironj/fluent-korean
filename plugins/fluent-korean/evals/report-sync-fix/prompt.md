---
description: A completion report, the usual place where telegraphic Korean shows up.
max_turns: 3
---

다음 작업을 방금 마쳤다고 가정하고, 나에게 보낼 완료 보고를 작성해줘. 상황: scripts/check-sync.sh가 실패해서 원인을 찾았더니 fluent-korean-not-coding.md 본문이 fluent-korean.md와 네 곳에서 달랐다('작업중'을 '작업 중'으로, 이중 공백 하나, 엠대시가 들어간 문구 하나, 서브에이전트 조항 누락). not-coding 판 본문을 coding 판에서 다시 생성해서 네 곳을 모두 맞췄고, check-sync.sh를 다시 실행해 통과를 확인했다. 커밋은 아직 하지 않았다.
