


## goland 

go提供的一种序列化结构,基于二进制,不过看样子好像不是非常流行. 还有prof什么之类的内容. 

具体使用方式如下. 

```go
func (_msg *ControlMessage) ToBuffer() []byte {
	var buf bytes.Buffer
	encoder := gob.NewEncoder(&buf)
	err := encoder.Encode(_msg)
	if err != nil {
		panic(err.Error())
	}
	bf := buf.Bytes()
	return bf
}

func ResolveControlMessage(_data []byte) *ControlMessage {
	_msg := &ControlMessage{}
	reader := bytes.NewReader(_data)

	decoder := gob.NewDecoder(reader)
	err := decoder.Decode(_msg)
	if err != nil {
		fmt.Println(err.Error())
	}
	return _msg
}


```
