<!--
.. title: Experiments with replicating elements of style with Transformer
.. slug: experiments-with-replicating-elements-of-style-with-transformer
.. date: 2019-11-09 17:24:31 UTC+01:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. status:
-->

I've been toying with this idea for a while and I think it might have some interest.

It is related to the concept of "Narrative Author" by Dehennin or the older "Implicit Author" in Literary Analysis terms.

I will try to pick it up more seriously in my free time, perhaps in collaboration with my dear partner, who was a better and more current background in Literary Analysis and Linguistics. It goes like this:

  * Transformer-based generative language models (GPT-2, BERT) can generate text (prompted or unprompted) with a degree of coherence not reachable by previous models, although still of course short of human performance.
  * Said models can be fine-tuned on smaller corpuses in the same language they were trained on. I've run some quick experiments fine-tuning GPT-2 on Jane Austen (unpublished) and [Philip K. Dick](link://slug/gpt-pkd). The results are only sometimes coherent, but they seem to maintain the original's *style* to some extent.

Thus the planned experiment:

  * Define a set of style markers in the context of the Narrative Author theory. These are markers present in texts that might be maintained or not maintained by the generative models trained in such texts.
  * Fine-tune models with these texts and generate prompted and unprompted texts.
  * Analyze which style markers remain present in the generated texts (or can be found by a reasonable reader, with or without knowledge of their generated nature).
