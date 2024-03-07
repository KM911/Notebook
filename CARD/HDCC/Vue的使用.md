
# element-plus的使用

## 表单输入框修改

表单中的输入框因为是内嵌属性，所以比较难修改，这时候

可以使用css的优先级，权值大的优先生效

解决：

往父级元素上加几个类名，让el-input的权值高一点，当然，也可以不用写，因为标签大都自带类名，F12检查一下。

## 表格数据多，但不能隐藏

数据过多不能隐藏？不妨试试官方提供的固定表头，这时候表格会出现滚动条,但是 不是页面的滚动条，是强迫症福音、

## 想要在修改之后立即显示

很简单，修改之后肯定是要发请求的对吧？

在请求成功之后，再次调用请求全部数据的方法即可实现实时响应？

## 为什么添加了router-view却不能跳转

首先检查有没有写错  to 的路径

其次检查  router-view 与 < 之间是否有空格，有空格也是会影响跳转的

## 我想要在组件切换的时候添加过渡动效



## 问题

这个也是容易的

你需要使用router-view（一对） 标签来包含标签 ```<tanslation>```
```<tanslation>``` 标签也是需要包含 compontent标签的

像这样：

```vue
<router-view v-slot="{ Component }">

	<transition name="slide-fade">

		  <component :is="Component" />
        
	</transition>

</router-view>
```

其中name属性可以自定义，与实际效果无关

还有几个css属性（重要）建议直接去官网查看

# 组合式API（setup）中常见问题

## 如何接受父组件传来的参数

使用 defineProps

```vue
const props = defineProps({
    
})
```

## 接受并存储token


```js

export function setToken(tokenKey, token) {
    return localStorage.setItem(tokenKey, tokenValue);
}

export function getToken(tokenKey) {
    return localStorage.getItem(tokenKey);
}

export function removeToken(tokenKey) {
    return localStorage.removeItem(tokenKey);
}

```

首先就是需要这三个函数了

在登陆返回的数据中  将 token 存储 在 localStorage中 tokenKey （存储的字段名称） 

建议设置为'token'

之后，还需要在进入其他页面时校验token，这个也容易，设置一首请求拦截器就可以了，因为你要访问页面,肯定是要发请求的嘞，在请求的时候设置请求头

例如：

![image-20230425161713873](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425161713873.png)

# 关于发送请求

## 第一步

首先要配置一首代理，其目的主要是 方便 和 跨域



如果用的是vite  那么就是在viteconfig

![image-20230425162103880](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425162103880.png)

这时候这个  /api就是指代 target 后的那个地址了

### 不设置会怎么样

你为什么不尝试一下

## 第一次封装axios

请注意：不要把 axios 添加到 main.js 中

至于为什么，建议尝试

把 axios 封装为 service

![image-20230425162603434](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425162603434.png)

baseURL每次都会在请求的时候添加到你写的路径前，这句话其实

### 第一次封装后请求的方式

![image-20230425162828160](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425162828160.png)

'/login'， 后面的那个参数是一个对象，是我要携带的请求体body

其他的请求方式我没有使用它进行尝试

## 第二次封装axios

为了增加代码的复用性，这次我把axios封装为一个返回值为一个promise对象的函数

**GET请求不带任何参数**

![image-20230425163219255](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425163219255.png)

**GET请求带路径参数**

![image-20230425163258316](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425163258316.png)

POST请求带请求体  data就是请求体中的数据

![image-20230425163415504](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425163415504.png)

常见的也就是这几种了

其他请求的写法也就是method不同


# 路由的使用

## router-view的用法

一句话概括，<router-view></router-view>中会显示与当前页面路径匹配的内容  当然 路径是要配置在路由中的

路由懒加载可以实现更少代码实现更好的效果，建议使用

![image-20230425163957579](C:\Users\HD\AppData\Roaming\Typora\typora-user-images\image-20230425163957579.png)

有时侯控制台报奇奇怪怪的错误，可能就是你的路径参数没写对

使用路由的好处我感受到的有  页面的切换更加的丝滑

router-link 虽然 与a标签本质相同，但是在切换页面的时候router-link却是 不刷新页面来切换内容的   它长和 ``<router-view>``搭配使用

## 关于路由守卫

前面我们设置了token ，路由守卫与之搭配就会实现在没有token的情况下无法根据网址栏进入页面，并且会重定向到登录页

这里说一下，重定向最好不要迭代，否则 页面很可能不报错，但是却加载失败

## 亟待解决的问题



# 关于一些Vue的功能实现

## 主题（背景颜色）变化

我需要一个能在每一个组件中都出现的值，这个值需要是响应式的，当它变化的时候触发事件，让对应组件的背景颜色发生改变

pinia+计算属性？ 还有事件的监听

具体实现：  

首先状态管理库可以为我们提供一个能够在全局使用的属性，并且我们也可以在任意一个组件中去修改它的值，而且还具有响应性。这样我们就是实现了第一步

接下来就是要根据开关的状态来改变状态管理库中的属性，这个直接在开关所在组件中用相关函数控制就可以了

为什么要用到computed，因为watch是不可以直接监听状态管理库中属性的状态的，所以我们要使用计算属性将它赋值给当前组件的某一个自定义的变量，然后监听该变量，以间接实现监听

最后就是样式的改变了，不用多说。

其实可以将这个方法封装到一个组件中去，看吧，如果你真的在很多地方都会用的话。

## 关于字符串转换的操作

直接写一个map集合，到时候直接 赋值吧
![image-20230714103923132](http://81.68.91.70/pg/image/KMnPKw4fI86r.png)
![image-20230714103951263](http://81.68.91.70/pg/image/KMDXi75xrDW8.png)

将原本是字符串的Answer的值转换为了Boolean类型的值

其他类似

# 后端

## 接受参数的注解

@Requestbody  用于接受json格式的请求数据，也就是前端直接携带一个data

@RequestParam 用于接收 路径后携带的参数 ？username = {useernmae}&  这种

@PathVarible 就是接受含在 url 中的 参数  /{parm}

## 我该如何设置session

首先应该有 HttpServletRequest 的对象

我们先假设  它的对象是  request

那么设置session 的方法就是  request.getSession.setAttribute( "字段名" ,  值 )

它是用来干嘛的呢？ 存储用户信息

为什么要存这个？我在登录之后访问页面，不能总让我说明我是谁

### token

接着上面的问题

token呢？  token是用户在登陆后，服务器返回给前端的数据，会通过拦截器添加在请求头中（而且会存储在本地），以便在之后的访问中确定用户的登录状态。

我为什么会问出这个问题？

因为我写的后台管理系统多，都是查询很多人的数据，所以会不明白session的更多信息。现在也不明白，上面的回答是基于现有知识

我是如何在前端页面中获得的个人信息？

我将一些需要的信息存储在了token中，在登陆时返回，这样我需要的时候直接到localStorage中拿了，当然我也可以根据用户名发送请求去获得。

## nginx做反向代理

 和我在 vite中做proxy的原理一致 标红区域为 服务器域名

![image-20230731181838987](http://81.68.91.70/pg/image/KMdaoPiYfysx.png)

做负载均衡 需要的配置文件

![image-20230731181801515](http://81.68.91.70/pg/image/KMf6NHasqE44.png)

### 负载均衡的策略

![image-20230731182130029](http://81.68.91.70/pg/image/KMEY2ST1N9yi.png)

## 关于从前端接收来的数据

如果属性不是很复杂，使用实体类接收，但是如果传过来的数据和实体类有共性但是差别比较大的话，使用DTO来接受，到 Service 层的时候再使用**对象属性拷贝** 传递到 实体类 的对象中

![image-20230801152226182](http://81.68.91.70/pg/image/KMve5NsZYDXV.png)

## 第一个知识点：ThreadLocal

![image-20230801183802651](http://81.68.91.70/pg/image/KMHEzP41H2IR.png)

客户端发起的每一个请求实际上都是一个新的线程

ThreadLocal实际上并不是一个线程，而是单个线程的一个存储器

感觉类似于前端的localstorage

## 第二个知识

为了防止日期格式的数据返回回前端的时候变成![image-20230801202847255](http://81.68.91.70/pg/image/KM0QKP0WjnSV.png)

这种格式，所以我们选择两种方法来解决这个问题

第一种就是在类中的日期类型的属性上加入注解 对日期进行格式化

@JsonFormat（pattern="yyyy-MM-dd HH:mm:ss"）

第二种就是在WebMvcConfiguration中扩展Spring MVC的消息转换器，统一对日期类型进行格式化的处理

## 关于缓存

![image-20230806164302226](http://81.68.91.70/pg/image/KMxx9y0HO4rs.png)

## 关于接口请求安全

了解 **timestamp** + nonce  

# 前端一些必要设置

去除多次点击会出现蓝色，很难看
但是如果你的页面需要让用户选择复制，那么请忽略这条，你展示代码，却不让人复制，不是让人很恼火吗？

```css
body{
	-webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
     user-select: none; 
}
```


## obsidian的样式失效问题

请不要毫无修饰的写出前一个尖括号,像下面这样
![[Pasted image 20231105155935.webp]]
如果你只想写一个，请使用```<font> ```包裹，不然下面的makedown语法产生的样式将全部失效
当你写尖括号的时候，请记得加反斜杠 它的意思是关闭标签，所以为什么出现问题，就不多说了。
<font/>  

