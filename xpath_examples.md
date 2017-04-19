- //*[@id="element_id"]
- //*[@id="fox"]/a
If the button is declared with the <button> tag and the button says “press me”, try this:
    - //button(contains(., 'press me')]

//input[@value='press me']

//*[text()='the visible text']

'//span[contains(text(), "Margi Malhotra")]'
the xpath can be replaced by //span[contains(., "Margi Malhotra")]
it can be replaced by //span[text()="Margi Malhotra "]

To find the Nth element, you must surround your XPath in ()s and then specify the Nth using [n], like this:
(//span[@title="Do ladke, dono bhadke!"])[2]

(//input[@type="text"])[4]  # find the fourth input element @type using text

//@title selects all elements which have attributes @title
//div selects all the div elements

//*[@id='app']/div/span[5] select fifth span element

//*[@id='app']/div/span[5]/../.. going two parents up

//meta[@name="og:title"][@content="WhatsApp Web"] # if you want to define multiple attributes

/bookstore/book[last()] # selecting the last element

//span[@*] matches span element that have at least one attribute of any kind

//book/title | //book/price # this is used for selecting several xpath



































