````col
```col-md
flexGrow=1
===
> [!note] 定义
> 跨域资源共享


> [!tip] 相关概念
> 
```
```col-md
flexGrow=1
===
> [!info] 别称
> 跨域

> [!cite]- 参考资料
> <% tp.file.cursor() %>
```
````


>[!note]- Cross-Origin Resource Sharing (CORS) 
>
>It is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.
>
>CORS also relies on a mechanism by which browsers make a "preflight" request to the server hosting the cross-origin resource, in order to check that the server will permit the actual request. In that preflight, the browser sends headers that indicate the HTTP method and headers that will be used in the actual request.
>
>For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts. For example, XMLHttpRequest and the Fetch API follow the same-origin policy. This means that a web application using those APIs can only request resources from the same origin the application was loaded from unless the response from other origins includes the right CORS headers.

## What requests use CORS?

This cross-origin sharing standard can enable cross-origin HTTP requests for:

Invocations of the XMLHttpRequest or Fetch APIs, as discussed above.
Web Fonts (for cross-domain font usage in @font-face within CSS), so that servers can deploy TrueType fonts that can only be loaded cross-origin and used by websites that are permitted to do so.
WebGL textures.
Images/video frames drawn to a canvas using drawImage().
CSS Shapes from images.

cause Axios was build by Fetch so you know , it will happend this. 


