---
file-created: 2023 11 23
last-modified: 2023 11 29
---

````col
```col-md
flexGrow=1
===
> [!note] 定义
> 本意 : 美人鱼 , 其实是一种图表绘制语法,可以在markdown绘制流程图,饼图等. 

> [!cite]- 参考资料
> [Mermaid Live Editor](https://mermaid.live/edit#pako:eNqFUDsKAkEMvcqSek8wtWBlZTtNnISdYZ0PISPIsnc3umqhiKke7xNeskCoxOBgSroXbNGXwSbUnJN-45NgCXEgvvC5tqceOcy16wf7Y8PbnTGVjcosE_9LwwjmsxBZ2eWueNDImT04g4Qye_BlNR92rcdrCeBUOo_QG6HyLuEkmF8kU9Iqh-34xw_WG5WOWVk)
> [Flowcharts Syntax ](https://mermaid.js.org/syntax/flowchart.html)
```
```col-md
flexGrow=1
===



> [!info] 优点
> 基于文本绘制,占据资源空间小


> [!error] 缺点
> 表达性较差,渲染效果未必好看.
```
````
## 实例图

方便你查看渲染的效果,一图胜千言
### Flow

```mermaid
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D[Laptop]
    C -->|Two| E[iPhone]
    C -->|Three| F[fa:fa-car Car]
```

### Class
```mermaid
classDiagram
    Animal <|-- Duck
    Animal <|-- Fish
    Animal <|-- Zebra
    Animal : +int age
    Animal : +String gender
    Animal: +isMammal()
    Animal: +mate()
    class Duck{
      +String beakColor
      +swim()
      +quack()
    }
    class Fish{
      -int sizeInFeet
      -canEat()
    }
    class Zebra{
      +bool is_wild
      +run()
    }
```

是一种描述的手段但是我确实用得非常少

```mermaid
classDiagram
    class Network{
        <span class="r">[[RPC]]</span>    
        application
        Transfer
        IP
        physical    
    }

```

### Sequence

```mermaid
sequenceDiagram
    Alice->>+John: Hello John, how are you?
    Alice->>+John: John, can you hear me?
    John-->>-Alice: Hi Alice, I can hear you!
    John-->>-Alice: I feel great!
```


```mermaid
sequenceDiagram
    CPU -->>+程序 : 处理程序
    程序 -->>+服务器 : 发送网络请求
    服务器 -->> 程序 : 返回响应结果
    CPU -->> 程序 : 处理程序
```

### Git
```mermaid
gitGraph
    commit
    commit
    branch develop
    checkout develop
    commit
    commit
    checkout main
    merge develop
    commit
    commit
```
### State
```mermaid
stateDiagram-v2
    [*] --> Still
    Still --> [*]
    Still --> Moving : line chat
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
```


```mermaid
stateDiagram
    direction LR
    start --> Download
    Download --> Parse
    Parse --> Store
    Store --> Download
    Store --> exit
```



### Pie
```mermaid
pie title Pets adopted by volunteers
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 15
```


### Gannt

甘特图 还是很有意思的.
```mermaid
gantt
    title A Gantt Diagram
    dateFormat  YYYY-MM-DD
    section Section
    A task           :a1, 2014-01-01, 30d
    Another task     :after a1  , 20d
    section Another
    Task in sec      :2014-01-12  , 12d
    another task      : 24d
```


### Er

说实话 我不知道ER图是什么 ? 
```mermaid
erDiagram
    CUSTOMER }|..|{ DELIVERY-ADDRESS : has
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER ||--o{ INVOICE : "liable for"
    DELIVERY-ADDRESS ||--o{ ORDER : receives
    INVOICE ||--|{ ORDER : covers
    ORDER ||--|{ ORDER-ITEM : includes
    PRODUCT-CATEGORY ||--|{ PRODUCT : contains
    PRODUCT ||--o{ ORDER-ITEM : "ordered in"
```



### Mindmap

为什么我们不适用xmind这样的软件呢? 

```mermaid
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectivness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid
```


### QudrantChart

最没用的一张图不是吗? 

```mermaid
quadrantChart
    title Reach and engagement of campaigns
    x-axis Low Reach --> High Reach
    y-axis Low Engagement --> High Engagement
    quadrant-1 We should expand
    quadrant-2 Need to promote
    quadrant-3 Re-evaluate
    quadrant-4 May be improved
    Campaign A: [0.3, 0.6]
    Campaign B: [0.45, 0.23]
    Campaign C: [0.57, 0.69]
    Campaign D: [0.78, 0.34]
    Campaign E: [0.40, 0.34]
    Campaign F: [0.35, 0.78]
```




```mermaid
quadrantChart
    Campaign A: [0.1, 0.2]
    Campaign B: [0.2, 0.5]
    Campaign C: [0.3, 0.7]
    Campaign D: [0.6, 0.9]
    
```
