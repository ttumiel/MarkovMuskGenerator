# Serverless Markov Chain Random Tweet Generator Cloud Function

Synthesize random tweets via Markov chain trained on existing Musk tweets. Deploys to a Google cloud function to generate these tweets via http requests.

[Visit the Demo Site](https://maybemusk.com/)

## Examples

> Sanctimonious journalists who appoint themselves protectors of the undead or your money back!

> Want Pravda to exist, write an article telling your readers to vote against it … 310 miles. Takes 0-60mph to 4.5 sec & top speed leaders over to pure electric.

> 2D streets and 3D buildings means bad traffic forever. Unless there is risk of climate science.

> Awesome non-linearities, such as tweeting on Ambien isn't wise.


## Deploy

```sh
gcloud functions deploy tweet_http --runtime python37 --trigger-http
```


Interestingly, one of the largest splits in the Markov chain is this:

```json
"would be": [
    "cool",
    "awesome",
    "great",
    "super",
    "much",
    "limited",
    "irresponsible",
    "Dick",
    "cool.",
    "no",
    "seriously",
    "amazing",
    "tricky",
    "too,",
    "ultra",
    "to",
    "awesome.",
    "most",
    "much",
    "unsafe.",
    "so",
    "really",
    "interesting.",
    "happy",
    "in",
    "suicide",
    "great.",
    "the",
    "much",
    "generous.",
    "a",
    "a",
    "fine,",
    "wrong.",
    "a",
    "better",
    "this",
    "greatly",
    "in",
    "wrong.",
    "a",
    "happy",
    "much",
    "conflicting",
    "a",
    "a",
    "long",
    "the"
]
```

Perfect for some interesting appraisals.
