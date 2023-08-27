## Basic API service for Box CRUD Operations

1. Get Authentication Token API - using username and password

<pre><code>
curl --location --request POST 'http://127.0.0.1:8000/store/auth_token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username":"store",
    "password":"admin@123"
}'
</code></pre>

2. Box Creation API

<pre><code>
curl --location --request POST 'http://127.0.0.1:8000/store/box/create/' \
--header 'Authorization: Token a1816b1a051ccaa128d7dc44320774a71abd5734' \
--header 'Content-Type: application/json' \
--data-raw '{
    "length":4,
    "width":2,
    "height":5
}'
</code></pre>

3. Box Listing API using Various filter

<pre><code>
curl --location --request GET 'http://127.0.0.1:8000/store/box/list/?length__lt=1000&area__gt=10&volume__lt=100&created_by=store' \
--header 'Authorization: Token a1816b1a051ccaa128d7dc44320774a71abd5734'
</code></pre>

Filters
1.length**lt
2.length**gt
3.width**lt
4.width**gt
5.height**lt
6.height**gt
7.created_by

4. Box Listing for specific user.
<pre><code>
curl --location --request GET 'http://127.0.0.1:8000/store/box/my_list/?length__lt=1000&area__gt=10&volume__lt=100&created_by=store' \
--header 'Authorization: Token a1816b1a051ccaa128d7dc44320774a71abd5734'
</code></pre>

Filters
1.length**lt
2.length**gt
3.width**lt
4.width**gt
5.height**lt
6.height**gt

4. Box Deletion API

<pre><code>
curl --location --request DELETE 'http://127.0.0.1:8000/store/box/delete/5' \
--header 'Authorization: Token a1816b1a051ccaa128d7dc44320774a71abd5734'
</code></pre>

5. Box Updation API

<pre><code>
curl --location --request PUT 'http://127.0.0.1:8000/store/box/update/7' \
--header 'Authorization: Token a1816b1a051ccaa128d7dc44320774a71abd5734' \
--header 'Content-Type: application/json' \
--data-raw '{
    "length":10,
    "width":3,
    "height":1
}'
</code></pre>
