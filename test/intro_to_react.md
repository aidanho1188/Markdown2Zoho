2024-01-29 
## Tags: #react
# Intro to react 
- Javascript tools
	- React(lib)
	- Vue(framework)
	- Angular(framework)
***
## React
* **purpose** - building interactive user interface with speed
#### Terms
* *components*
* *declarative*
* *compose* - stick thing together
* props - input to react components
	* 
```javascript
// props
function getImageComponent() {
	return [{
	src: "https://google.com/images",
	altText: "image stuff",
	width: 300,
	height: 300
	},
	{
	src: "https://facebook.com/images",
	altText: "image stuff",
	width: 300,
	height: 300
	}]
}
const imageData = getImageComponent();
// react component: src is props, imageData.src is the value of props
imageData.map((data) => {
	return <Image src={imageData.src} altText={imageData.altText} width={imageData.width} height={imageData.height />
})

// output of compnent we declared
return <img scr="" altText="" width="" height""/>

```
* state - current thing that the app is doing
* jsx - look like html when compiled it become raw javascript
* build/compile - 
* children
* controlled vs uncontrolled
* keys
* refs
***
## Web application example
* ![[Pasted image 20240129192829.png]]
* rendering flow, data downward, lifecycle
	* state/prop change => render and rerender the other thing needing updates
	* when a state changes, trigger other possible thing to turn on
	* react updates your DOM when it rerender
	* diffing algo under the hood
	* **Shadow DOM** - when done, it goes and replace or put it in the real DOM
*
***
### package
* eslint - help prevent errors and bug, you must fix it before you can commit

### webpack 
* the tool to pack the whole app
* under the hood to build the compile

# This is a table

| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |
# This is a quote
> Hello world!


## Related Ideas [[]] 
## Source [[]]
 -  