## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:request
- Could you please give me some news about [Revolut](target)?
- I want some information about [Bitcoin](target).
- I am looking for breaking news about [Apple](target).
- Do you have any news about [Microsoft](target)?
- Could you please send me some news about [Revolut](target)?
- Do you know anything about [Revolut](target)?
- What is the latest news about [Ethereum](target)?
- I need to get the latest news on [PlusOne](target).
- Please send me the latest news about [FinTech](target).

## intent:details
- Could you please get me the [title](news_detail) of [first news]{"entity":"sent_news", "value":"1"} you just sent?
- Could you please get me the [content](news_detail) of [second news]{"entity":"sent_news", "value":"2"} you just sent?
- Could you please get me the [publication](news_detail) date of [first one]{"entity":"sent_news",
    "value":"1"} you just sent?
- Give me [title](news_detail) of latest news about [FinTech](target).
- Give me [publication date](news_detail) of latest news about [Revolut](target).
- Give me [source](news_detail) of latest news about [Apple](target).
- Give me [content](news_detail) of latest news about [Microsoft](target).
- Do you know what is the [title](news_detail) of latest news about [Bitcoin](target)?
- Do you know what is the [content](news_detail) of latest news about [Bitcoin](target)?
- Do you know what is the [source](news_detail) of latest news about [Bitcoin](target)?
- and the second one?
- and the first one?
- what about the [first one]{"entity":"sent_news", "value":"1"}?
- what about the [second one]{"entity":"sent_news", "value":"2"}?
- what about the [third one]{"entity":"sent_news", "value":"1"}?
- what about the [second]{"entity":"sent_news", "value":"2"}?
- what about the [third]{"entity":"sent_news", "value":"3"}?

## intent:request+details
- Please give me [title](news_detail) of latest news about [Revolut](target).
- What is the [publication date](news_detail) of latest news about [Apple](target)?
- What is [content](news_detail) of latest news about [Microsoft](target)

## intent:link
- please send me the link
- link please
- Could you also send me the link?
- I also need the link to the news
- Also need the link

## intent:affirm+link
- yes, also please send me the link
- indeed and the link please
- of course. Could you also send me the link?
- that sounds good. I also need the link to the news
- correct. Also need the link
