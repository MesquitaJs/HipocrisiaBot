###########################################################################
#                           EFIM, O BOT                                   #
#                           @Mesquita_js                                  #
#          captura o texto do tweet(tweepy) e escreve na imagem(PIL)      #
###########################################################################

#-------------------------------------------------------------------------------------------------------
import tweepy
import time
from PIL import Image, ImageDraw, ImageFont, ImageOps
import re
import textwrap

#credenciais
auth = tweepy.OAuthHandler("n1Iv8XOUVJpGD7roDPtJJgb0A", "dpUUgamEaAXbN7BaH2kukUHPK057JiMzprSwkdXUX12ws3x8C3")
auth.set_access_token("1293631930387304448-1PQ52Rj0EUBgKRcUgSpKUKdaqxHRZs", "jilgV99MWC7rckBQvLoX0Q1ybbuN4mG4Ws8lK2aDABefk")

#objeto
api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=True)  

#classe
class StreamingListener(tweepy.StreamListener):
    def on_status(self, status):
        print("tweet hipocrita: " + status.text)
        fonte = ImageFont.truetype("fonts/times_roman.ttf", 35)
        search = "#HipoBot"
        num = 1
        img = Image.open("images/hipocrisia_big.png")
        draw = ImageDraw.Draw(img)

        for tweet in tweepy.Cursor(api.search, search).items(num):
            try:
                print("nome do usuario: @" + tweet.user.screen_name)
                temp_tweet = api.get_status(tweet.id, tweet_mode='extended')._json['full_text'].replace("#HipoBot", "").replace("#hipobot", " ").replace("#HIPOBOT", " ").replace("#hipoBot", "")
                #expressão regular >aqui<
                print(str(temp_tweet))
                draw.text(xy=(550, 15), text=textwrap.fill('"' + str(temp_tweet).lower() + '"', 28), fill=(255, 255, 255), font=fonte)
                img.save('images/botGen.png')
                api.update_with_media('images/botGen.png', status="@" + tweet.user.screen_name + " ", in_reply_to_status_id=tweet.id)
                print("tuite enviado corretamente")
                time.sleep(5)
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

if __name__ == "__main__":
    streamer = StreamingListener()
    same_api = api
    streaming = tweepy.Stream(auth=same_api.auth, listener=StreamingListener())
    streaming.filter(track=['#HipoBot'])