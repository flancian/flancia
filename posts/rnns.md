<!--
.. title: RNNs
.. slug: rnns
.. date: 2019-03-23 16:40:45 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. status:
-->

I read "[The Unreasonable Effectiveness of Recurrent Neural Networks][1]" by Andrej Karpathy this weekend. I saw it recommended/linked several times so I added it to my ML to-do/to-read list, and I've just gotten to it. Some highlights I copy/pasted into Keep follow:

> As you might expect, the sequence regime of operation is much more powerful compared to fixed networks that are doomed from the get-go by a fixed number of computational steps, and hence also much more appealing for those of us who aspire to build more intelligent systems.

Then:

> Moreover, as we’ll see in a bit, RNNs combine the input vector with their state vector with a fixed (but learned) function to produce a new state vector. This can in programming terms be interpreted as running a fixed program with certain inputs and some internal variables. Viewed this way, RNNs essentially describe programs. In fact, it is known that RNNs are Turing-Complete in the sense that they can to simulate arbitrary programs (with proper weights). 
> If training vanilla neural nets is optimization over functions, training recurrent nets is optimization over programs.

Interesting. Karpathy does add a caveat about not reading too much into this, and I can see how this "universal program approximation" thing of RNNs has also other more indirect ties to "Turing completeness", in the sense that people sometimes get hung up on Turing completeness when in many cases it just isn't very relevant -- as in, it's a pretty low bar for a programming language or platform in the day-to-day and it doesn't mean much in practice. Still, the fact that RNNs trained character-by-character are able to pick up greater and greater levels of structure seems very promising. I found the visualizations of per-neuron activity very illuminating: Karpathy finds a neuron that "learns" to be "on" when inside a quotation, and another that gets activated as the text gets closer to where a newline would usually appear. This is all structure that a programmer would likely think about and code by hand they had to hand-code a text generator, and the network is just learning it independently from data.

The article is from 2015, but some people seem to think it's a bit dated by now -- not in its basic approach necessarily, but rather because convolutions have taken over from RNNs/LSTM in many domains. [gwern][2] left [this comment][3] in Hacker News (I swear I'm not stalking him, he just keeps popping up in the stuff I read):

> If this were written today, Karpathy would have to call it "The Unreasonable Effectiveness of Convolutions". Since 2015, convolutions, causal or dilated convolutions, and especially convolutions with attention like the Transformer, have made remarkable inroads onto RNN territory and are now SOTA for most (all?) sequence-related tasks. Apparently RNNs just don't make very good use of that recurrency & hidden memory, and the non-locality & easy optimization of convolutions allow for much better performance through faster training & bigger models. Who knew?"

My current plan is to experiment a bit with RNNs/LSTM and then move on to convolutions.

[1]: http://karpathy.github.io/2015/05/21/rnn-effectiveness/
[2]: link://slug/gwern
[3]: https://news.ycombinator.com/item?id=19070547
