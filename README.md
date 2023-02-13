# Questions Banks Blog
<p>
This App have build With:
</p>
<ul>
    <li>Django</li>
    <li>Django Rest Framework</li>
    <li>Rest Framework SimpleJWT</li>
</ul>
<p>
And It has some API EndPoint for Question CRUD and Getting Set of Questions.
Some API EndPoint for creating and Updating Question Answers
</p>

## TODO
- [x] Question Getting, Adding, Updating, Deleting and Retrieving EndPoint
- [x] Answer Creating EndPoint
- [ ] Answer Viewing for that user (EndPoint)
- [ ] Answer CRUD EndPoint (except Creating because is already done)
- [ ] TestCase For Answers
- [ ] Customize User Model

## EndPoints
<ul>
    <li>/api/questions/ ==> listing questions</li>
    <li>/api/questions/&lt;question_id&gt;/ ==> specified question and CRUD</li>
    <li>/api/answers/ ==> Listing Answers</li>
    <li>/api/answers/&lt;answers_id&gt;/ ==> Specified Answer And CRUD</li>
    <li>/jwt-auth/token/ ==> Authentication User, Get Token</li>
    <li>/jwt-auth/refresh/ ==> Get New Access Token by given Refresh Token</li>
    <li>/jwt-auth/verify/ ==> Checking Refresh Token validation</li>
</ul>