# Architecture

```{mermaid}
flowchart TD
    Src["/tiny/ tree"] --> Pack[pack]
    Pack --> Clone[full copy]
    Pack --> Child[child]
    Child --> Soft[stage baby / interactions 0]
    Child --> Drop[unlink media]
    Soft --> Out[baby tree]
    Drop --> Out
```
