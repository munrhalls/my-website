{% extends "base.html" %}

{% block page_content %}

<div class="col-md-8 offset-md-2">

    <h1>Blog Index</h1>

    <hr>

    {% for post in posts %}

    <h2><a href="{% url 'blog_detail' post.pk%}">{{ post.title }}</a></h2>

    <small>

        {{ post.created_on.date }} |&nbsp;

        Categories:&nbsp;

        {% for category in post.categories.all %}

        <a href="{% url 'blog_category' category.name %}">

            {{ category.name }}

        </a>&nbsp;

        {% endfor %}

    </small>

    <p>{{ post.body | slice:":400" }}...</p>

    {% endfor %}

</div>

{% endblock %}