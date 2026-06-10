<!--
html是网页的骨架，也是我们学习web开发最坚实的基础
__author__ = '伟大的小熊猫'
-->

<!--
<html>
    <head>
        <title>这是小熊猫的网站</title>
    </head>
    <body>
        <h1>你好，世界</h1>
    </body>
</html>
-->

<!--
<!DOCTYPE html>
<html>
<head>
    <title>小熊猫</title>
    <style>
    h1{
        color:#ff3333;
        font-size:48px;
        text-shadow: 3px 3px 3px #666666;;
    }
    </style>
</head>
<body>
    <h1>我是小熊猫，很高兴见到你</h1>
</body>
</html>
-->

<!DOCTYPE html>
<html>
<head>
    <title>小熊猫</title>
    <style>
    h1{
        color:#ff3333;
        font-size:48px;
        text-shadow: 3px 3px 3px #666666;;
    }
    </style>
    <script>
    var x=0
    function change(){
    var title = document.getElementsByTagName('h1')[0];
    var randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
    if (x%2==0) {
        title.style.color = '#ff3333';
    }
    else {
        title.style.color = randomColor;
    }
    x+=1
    }
    </script>
</head>
<body>
    <h1>我是小熊猫，很高兴见到你</h1>
    <button onclick="change()">点我变色</button>
</body>
</html>