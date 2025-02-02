## 代码说明
该脚本调用API获取推主发表的推文的所有信息，运行后会获得一个X_{name}.jsonl文件。若今天日期是2025年2月1日，则一般会采集到2024年1月（经验来源：musk和sam）

代码目的是采集AI领域相关的大V的推特信息，从而了解这些有影响力的人的观点。目标是判断AI发展趋势，尤其是商业模式的讨论，能否实现收入增长等。

需要改进：1. 仍未对采集到的信息做扁平化处理 2. 虽然有url，但仍未找到获取图片、视频等media的手段 3. 未对大V名单做进一步的筛选 4. 未涉及大V推文的评论区数据。

## AI大V名单：（可考中文网站来源是赛博禅心微信公众号）
1. Sam Altman (@sama) 

  - Foundetr of OpenAI 

  - Former president of Y Combinator

2. Yann LeCun (@ylecun) 

  - Professor at NYU

  - Chief AI Scientist at Meta

3. Andrew Ng (@AndrewYNg) 

  - Co-Founder of Coursera

  - Stanford CS adjunct faculty

  - Former head of Baidu AI Group/Google Brain

4. François Chollet (@fchollet) 

  - Deep learning at Google

  - Creator of Keras

  - Author of 'Deep Learning with Python'

5. Karen Hao 郝珂灵 (@_KarenHao) 

  - A.I. Journalist at WSJ 

  - National magazine award winner

6. Andrej Karpathy (@karpathy) 

  - YouTuber, Blogger, Influencer

  - Previously Director of AI at Tesla, OpenAI

7. Jürgen Schmidhuber (@SchmidhuberAI) 

  - Co-director of the Dalle Molle Institute for Artificial Intelligence Research

  - He has been referred to as "father of modern AI" and "father of deep learning"

8. Sara Hooker (@sarahookr) 

  - Head of AI at Cohere 

  - Formerly Research at Google Brain

9. Demis Hassabis (@demishassabis) 

  - Founder & CEO of DeepMind and Isomorphic Labs

10. Sarah Guo (@saranormous) 

  - Founder of Conviction A.I., Starup Investor

  - Former partner at Greylock

11. David Hardmaru (@hardmaru) 

  - Head of Prompt Engineering at Stability AI

  - Former Research Scientist at Google Brain

12. Lilian Weng (@lilianweng) 

  - Applied AI Lead at OpenAI 

13. Oriol Vinyals (@OriolVinyalsML) 

  - Research Director & Deep Learning Lead at DeepMind

  - Led AlphaStar, AlphaFold, AlphaCode, WaveNet, seq2seq, etc

  - Former research scientist at Google Brain

14. Michael Black (@Michael_J_Black) 

  - Director at Max Planck Institute for Intelligent Systems 

  - Chief Scientist at Meshcapade

15. Jeff Dean (@JeffDean) 

  - Senior Fellow & SVP, Google Research and AI

  - Co-designer/implementor of software systems like TensorFlow, MapReduce, Bigtable, Spanner, etc

16. Ian Goodfellow (@goodfellow_ian) 

  - Research Scientist at DeepMind

  - Inventor of GANs

  - Lead author of http://deeplearningbook.org

17. Aakanksha Chowdhery (@achowdhery) 

  - PaLM Lead at Google Brain 

18. Peter H. Diamandis, MD (@PeterDiamandis) 

  - Founder of Singularity University, Xprize, Fountainlife

  - Entrepreneur, Investor and Author

19. Gary Marcus (@GaryMarcus) 

  - Author of Rebooting.AI & Guitar Zero

  - Founder of Geometric Intelligence (acq. by Uber) & RobustAI

20. Lucas Beyer (@giffmana)

  - Researcher at Google Brain in Zürich

21. Sebastian Raschka (@rasbt) 

  - Author of Ahead of AI 

  - Machine learning & AI researcher

22. Cassie Kozyrkov (@quaesita) 

  - Chief Decision Scientist at Google 

23. Kate Kaye (@KateKayeReports) 

  - Independent Journalist 

  - Formerly Protocol)

24. Emad (@EMostaque) 

  - Founder of Stability A.I. 

25. Fei-Fei Li (@drfeifei) 

  - Co-Director at Stanford Human-Centered Artificial Intelligence 

  - Co-Founder and Chair of AI4Allorg

26. Jim Fan (@DrJimFan) 

  - AI Scientist at Nvidia 

27. Elvis Saravia (@omarsar0 ) 

  - Builder of DAIR AI

  - Former Scientist at Meta AI and Elastic

28. Connie Chan (@conniechan) 

  - General Partner at a16z 

29. Hugo Larochelle (@hugo_larochelle) 

  - Researcher at Google Brain

  - Machine learning professor

  - Ex-Twitter Cortex 

30. Benj Edwards (@benjedwards) 

  - AI and ML Reporter, Ars Technica 

  - Tech Historian

31. Becca Szkutak (@rebecca_szkutak) 

  - Journalist at Techcrunch 

32. Sergey Levine (@svlevine) 

  - Professor at UCBerkeley 

33. Eric Schmidt (@ericschmidt) 

  - Former Google CEO 

34. Ilya Sutskever (@ilyasut) 

  - AGI at OpenAI 

35. Patrick Mineault (@patrickmineault) 

  - Formerly Building 8 

  - Former Engineer at Google

36. Natasha Jaques (@natashajaques)

  - Senior Research Scientist at Google AI and Berkeley AI

37. Pieter Abbeel (@pabbeel)

  - Professor at Berkeley

  - Founder of Covariant & Gradescope

  - The Robot Brains Podcast Host

  - Investment Partner at AIX Ventures 

38. Eliezer Yudkowsky (@ESYudkowsky) 

  - Co-Founder at Machine Intelligence Research Institute 

39. Geoffrey Hinton (@geoffreyhinton) 

  - Professor at University of Toronto

  - Co-Founder and Chief Scientific Advisor of the Vector Institute

40. Brett Winton (@wintonARK) 

  - Chief Futurist at Ark Invest

41. Jeff Clune (@jeffclune) 

  - Associate Professor at University British Columbia

  -  Faculty Member of Vector Institute

42. Sridhar Ramaswamy (@RamaswmySridhar) 

  - Co-Founder of Neeva & NXYZ Data

  - Venture Partner at Greylock

  - Former SVP at Google 

43. Ben Tossell (@bentossell) 

  - Author of Ben's Bites 

44. John Schulman (@johnschulman2) 

  - Co-Founder of OpenAI 

45. Ahsen Khaliq (@_akhaliq) 

  - Author of AK’s Substack

  - Founder of Gradio, acquired by HuggingFace

46. Quoc Le (@quocleix) 

  - Principal Scientist at Google Brain 

47. Jack Clark (@jackclarkSF) 

  - Founder of Anthropic AI 

  - Co-Chair at Indexing AI

  - Formerly at OpenAI

48. merve (@mervenoyann) 

  - Hugging Face (Merve Noyan) 

49. David (@DavidSHolz) 

  - Founder of Midjourney and Leap Motion

  - Formerly at NASA and Max Planck Institute

50. Nathan Lambert (@natolambert) 

  - Machine Learning Scientist at Hugging Face 

  - Democratizing Automation

51. Richard Socher (@RichardSocher) 

  - CEO at You.com 

52. Mustafa Suleyman (@mustafasuleymn) 

  - Co-Founder & CEO of InflectionAI 

  - Co-Founder of DeepMind

  - Venture Partner at Greylock

  - Former VP of AI at Google

53. Zoubin Ghahramani (@ZoubinGhahrama1) 

  - VP of Research at Google Brain

  - Professor at University of Cambridge

54. Nathan Benaich (@nathanbenaich) 

  - Author of Guide to AI 

55. John McDonnell (@johnvmcdonnell) 

  - Formerly at Stitch Fix, Square, Gureckis Lab

56. Bojan Tunguz (@tunguz) 

  - Senior Systems Software Engineer (Machine Learning) at Nvidia 

57. Ben Goertzel (@bengoertzel) 

  - CEO at Singularity 

58. Chris Olah (@ch402) 

  - Founder of Anthropic AI 

  - Formerly at OpenAI Clarity Team, Google Brain and Distill Pub

59. Ksenia Se (@Kseniase_) 

  - Author of TheSequence 

60. Paul Graham (@paulg) 

  - Venture Capitalist 

61. Russ Salakhutdinov (@rsalakhu) 

  - Former Apple AI

62. Greg Brockman (@gdb) 

  - President and Co-Founder of OpenAI 

63. Vivek Natarajan (@vivnat) 

  - Advancing Medical AI at Google AI 

  - Former Researcher at Meta AI

64. Brian X. Chen (@bxchen) 

  - Journalist at New York Times

65. Anima Anandkumar (@AnimaAnandkumar) 

  - Professor at CalTech

  - Senior Director of AI Research at NVIDIA

  - Former Principal Scientist at AWS Cloud

66. Jeffrey Towson 陶迅 (@JeffreyTowson) 

  - Consultant 

67. Thomas Wolf (@Thom_Wolf) 

  - Co-Founder of Hugging Face 

68. John Platt (@johnplattml) 

  - Director of Applied Science at Google AI 

69. Samanyou Garg (@SamanyouGarg) 

  - Founder & CEO of Writesonic 

70. Kirk Bourne (@KirkDBorne) 

  - Data Scientist at DataPrime

71. Alberto Romero (@Alber_RomGar) 

  - Author of The Algorithmic Bridge

  - Analyst at CambrianAI

72. Matthew Hutson (@SilverJacket) 

  - A.I. Freelance journalists 

73. Tim Scarfe (@ecsquendor) 

  - YouTuber on Machine Learning 

74. Jordan Burgess (@jordnb) 

  - Co-Founder of Humanloop 

75. David Luan (@jluan) 

  - Founder of Adept AI 

76. Connor Leahy (@NPCollapse) 

  - Founder of Conjecture & EleutherAI

77. Naveen Rao (@NaveenGRao) 

  - Co-Founder & CEO of MosaicML 

  - Former Nervana/IntelAI

78. Azeem Azhar (@azeem) 

  - Author of Exponential View 

79. Suhail Doshi (@Suhail) 

  - Founder of Playground.AI & MixPanel

80. Max Jaderberg (@maxjaderberg) 

  - Director of Machine Learning at IsomorphicLabs

  - Former research scientist at DeepMind

  - Co-founder Vision Factory (acquired by Google)

81. Kyle Wiggers (@Kyle_L_Wiggers) 

  - Tech AI Journalist at TechCrunch

82. Wei Xu (@cocoweixu) 

  - Assistant Professor in CS at GeorgiaTech

83. Aidan Gomez (@aidangomezzz) 

  - Co-Founder & CEO of Cohere 

84. Alexandr Wang (@alexandr_wang) 

  - Founder of Scale AI 

85. Caiming Xiong (@CaimingXiong) 

  - VP of AI at Salesforce

86. Yi Ma (@YiMaTweets) 

  - Professor of EECS UC Berkeley & IDS HKU

87. Misha Denil (@notmisha)

  - Research Scientist at DeepMind 

88. Peter Lee (@peteratmsr) 

  - Corporate Vice President at Microsoft Research 

89. Shivon Zilis (@shivon) 

  - Director of operations and special projects at Neuralink

90. Jacky Liang (@jackyliang42) 

  - PhD Student at CMU

  - Author of Last Week in AI 

91. Vin Vashishta (@v_vashishta) 

  - High ROI Data Science 

92. Xuedong Huang (@xdh) 

  - Technical Fellow atMicrosoft, Azure AI 

93. Hannah Fry (@FryRsquared) 

  - Tech Author 

94. Ravi Mhatre (@ravi_lsvp) 

  - Lightspeed Ventures 

95. clem (@ClementDelangue) 

  - Co-Founder & CEO of Hugging Face 

  - Founder of MoodStocks, acquired by Google

96. Hattie Zhou (@oh_that_hat) 

  - PhD Student at Université de Montréal and Mila 

97. Sapna Maheshwari (@sapna) 

  -  Journalist at New York Times

98. Vidhi Lalchand (@VRLalchand) 

  - PhD student in Machine Learning at Cambridge

99. Santiago L Valdarrama (@svpino) 

  - Machine Learning Freelancer and Technical Writer

100. Vincent Boucher (@ceobillionaire) 

  - President of Montreal AI

101. Yannic Kilcher (@ykilcher) 

  - YouTube Creator 

102. Matt Bornstein (@BornsteinMatt) 

  - Partner at a16z 

103. Lachy Groom (@lachygroom) 

  - Angel Investor

  - Founder BleedingEdge

  - Formerly at Stripe

104. Riley Goodside (@goodside) 

  - Chief Scientist at Scale AI

  - Former Data Scientist at OkCupid and Grindr

105. Amjad Masad (@amasad) 

  - CEO & Head of Engineering of Replit

106. Noam Brown (@polynoamial)

  - AI Research Scientist at MetaAI

  - Co-created Libratus/Pluribus, the first superhuman no-limit poker AIs

  - Co-created CICERO

107. Shital Shah (@sytelus)

  - Machine Intelligence, Deep Learning, Neural Architectures


## 注意
推文一般分一下几种情况：
1. 直接推文，可能含语言、文字、视频
2. 转发，直接转发原推文
3. 引用，会有作者自己的观点，可能含有语言、文字、视频



在社交媒体平台Twitter（现X）中，retweeted 和 quoted 是两种不同的操作方式，它们的主要区别在于是否添加个人评论以及内容的呈现方式：
1. Retweet（直接转发）
定义：Retweet 是将某条推文原封不动地转发到自己的时间线中，让自己的关注者也能看到这条推文。
特点：
不添加任何个人评论，直接分享原始推文。
原始推文的作者会被明确标注。
操作方式：点击推文下方的“Retweet”图标，选择“Retweet”即可。
1. Quote Tweet（引用转发）
定义：Quote Tweet 是在转发推文时添加自己的评论或观点。
特点：
可以在转发时添加自己的评论、观点或进一步的解释。
原始推文会显示在你的评论下方，方便读者快速了解上下文。
适合在分享内容的同时表达自己的看法，甚至可以对内容进行扩展或反驳。

## 数据示例如下，需统一格式，扁平化处理：


{'tweet_id': '1885214631704031690',
 'bookmarks': 0,
 'created_at': 'Fri Jan 31 06:32:48 +0000 2025',
 'favorites': 0,
 'text': 'RT @MarioNawfal: 🚨🇺🇸TESLA NAMED A TOP 100 EMPLOYER OF CHOICE IN 2024\n\nTesla’s Form 10-K filing reveals the company earned a spot among the…',
 'lang': 'en',
 'views': '13',
 'quotes': 0,
 'entities': {'hashtags': [],
  'symbols': [],
  'timestamps': [],
  'urls': [],
  'user_mentions': [{'id_str': '1319287761048723458',
    'name': 'Mario Nawfal',
    'screen_name': 'MarioNawfal'}]},
 'replies': 0,
 'retweets': 553,
 'conversation_id': '1885214631704031690',
 'media': [],
 'author': {'rest_id': '44196397',
  'name': 'Elon Musk',
  'screen_name': 'elonmusk',
  'avatar': 'https://pbs.twimg.com/profile_images/1874558173962481664/8HSTqIlD_normal.jpg',
  'blue_verified': True},
 'retweeted': {'id': '1885173661591601397'},
 'retweeted_tweet': {'tweet_id': '1885173661591601397',
  'bookmarks': 85,
  'created_at': 'Fri Jan 31 03:50:00 +0000 2025',
  'favorites': 3821,
  'text': '🚨🇺🇸TESLA NAMED A TOP 100 EMPLOYER OF CHOICE IN 2024\n\nTesla’s Form 10-K filing reveals the company earned a spot among the Top 100 Employers of Choice in the 2024 American Opportunity Index.\n\nBy the end of 2024, Tesla’s global workforce reached 125,665 employees, solidifying its https://t.co/jjaHnDiD8b',
  'lang': 'en',
  'views': '786964',
  'quotes': 26,
  'entities': {'hashtags': [],
   'media': [{'display_url': 'pic.x.com/jjaHnDiD8b',
     'expanded_url': 'https://x.com/MarioNawfal/status/1885173661591601397/photo/1',
     'id_str': '1885167310870028288',
     'indices': [279, 302],
     'media_key': '3_1885167310870028288',
     'media_url_https': 'https://pbs.twimg.com/media/Gil1rmKWIAAtGPk.jpg',
     'type': 'photo',
     'url': 'https://t.co/jjaHnDiD8b',
     'ext_media_availability': {'status': 'Available'},
     'features': {'large': {'faces': []},
      'medium': {'faces': []},
      'small': {'faces': []},
      'orig': {'faces': []}},
     'sizes': {'large': {'h': 559, 'w': 1116, 'resize': 'fit'},
      'medium': {'h': 559, 'w': 1116, 'resize': 'fit'},
      'small': {'h': 341, 'w': 680, 'resize': 'fit'},
      'thumb': {'h': 150, 'w': 150, 'resize': 'crop'}},
     'original_info': {'height': 559,
      'width': 1116,
      'focus_rects': [{'x': 0, 'y': 0, 'w': 998, 'h': 559},
       {'x': 0, 'y': 0, 'w': 559, 'h': 559},
       {'x': 0, 'y': 0, 'w': 490, 'h': 559},
       {'x': 0, 'y': 0, 'w': 280, 'h': 559},
       {'x': 0, 'y': 0, 'w': 1116, 'h': 559}]},
     'media_results': {'result': {'media_key': '3_1885167310870028288'}}},
    {'display_url': 'pic.x.com/jjaHnDiD8b',
     'expanded_url': 'https://x.com/MarioNawfal/status/1885173661591601397/photo/1',
     'id_str': '1885167534833360897',
     'indices': [279, 302],
     'media_key': '3_1885167534833360897',
     'media_url_https': 'https://pbs.twimg.com/media/Gil14ofXYAEV3oc.jpg',
     'type': 'photo',
     'url': 'https://t.co/jjaHnDiD8b',
     'ext_media_availability': {'status': 'Available'},
     'features': {'large': {'faces': []},
      'medium': {'faces': []},
      'small': {'faces': []},
      'orig': {'faces': []}},
     'sizes': {'large': {'h': 600, 'w': 900, 'resize': 'fit'},
      'medium': {'h': 600, 'w': 900, 'resize': 'fit'},
      'small': {'h': 453, 'w': 680, 'resize': 'fit'},
      'thumb': {'h': 150, 'w': 150, 'resize': 'crop'}},
     'original_info': {'height': 600,
      'width': 900,
      'focus_rects': [{'x': 0, 'y': 96, 'w': 900, 'h': 504},
       {'x': 300, 'y': 0, 'w': 600, 'h': 600},
       {'x': 374, 'y': 0, 'w': 526, 'h': 600},
       {'x': 592, 'y': 0, 'w': 300, 'h': 600},
       {'x': 0, 'y': 0, 'w': 900, 'h': 600}]},
     'media_results': {'result': {'media_key': '3_1885167534833360897'}}}],
   'symbols': [],
   'timestamps': [],
   'urls': [],
   'user_mentions': []},
  'replies': 303,
  'retweets': 553,
  'conversation_id': '1885173661591601397',
  'author': {'rest_id': '1319287761048723458',
   'name': 'Mario Nawfal',
   'screen_name': 'MarioNawfal',
   'avatar': 'https://pbs.twimg.com/profile_images/1670905743619268609/pYItlWat_normal.jpg',
   'blue_verified': True},
  'media': {'photo': [{'media_url_https': 'https://pbs.twimg.com/media/Gil1rmKWIAAtGPk.jpg',
     'id': '1885167310870028288',
     'sizes': {'h': 559, 'w': 1116}},
    {'media_url_https': 'https://pbs.twimg.com/media/Gil14ofXYAEV3oc.jpg',
     'id': '1885167534833360897',
     'sizes': {'h': 600, 'w': 900}}]}}}
马斯克自己的推文是转发了该retweeted_tweet

kimi：
由于网络原因，我无法直接访问或解析这些链接的内容。这可能是由于链接本身的问题（例如链接已失效或格式不正确），也可能是网络连接问题导致的。如果你需要这些链接的具体内容，建议你检查链接的合法性，并尝试在浏览器中直接访问它们。如果问题仍然存在，可以稍后再试，或者检查网络连接是否正常。
不过，我可以帮你解析你提供的数据格式，重点关注作者所说的内容、他转发的内容（retweet）以及媒体的格式。
解析数据
以下是对你提供的数据的解析：
1. 作者信息
作者名称：Elon Musk（保留）
作者推特用户名：@elonmusk（保留）
作者头像：https://pbs.twimg.com/profile_images/1874558173962481664/8HSTqIlD_normal.jpg
是否蓝V认证：是（blue_verified 为 True）
1. 作者所说的内容
推文内容：RT @MarioNawfal: 🚨🇺🇸TESLA NAMED A TOP 100 EMPLOYER OF CHOICE IN 2024\n\nTesla’s Form 10-K filing reveals the company earned a spot among the…（若不是转发rewteet，即保留）
推文创建时间：Fri Jan 31 06:32:48 +0000 2025（保留）
推文ID：1885214631704031690                        （保留）
语言：en（英语）     
互动数据：           （保留）
点赞数：0
回复数：0
转发数：553
引用数：0
浏览量：13
1. 作者转发的内容（Retweet）【保留】
转发的推文ID：1885173661591601397
转发的推文内容：
复制
🚨🇺🇸TESLA NAMED A TOP 100 EMPLOYER OF CHOICE IN 2024

Tesla’s Form 10-K filing reveals the company earned a spot among the Top 100 Employers of Choice in the 2024 American Opportunity Index.

By the end of 2024, Tesla’s global workforce reached 125,665 employees, solidifying its <url id="" type="url" status="parsing" title="" wc="0">https://t.co/jjaHnDiD8b&#39;,</url>
转发的推文创建时间：Fri Jan 31 03:50:00 +0000 2025
转发的推文作者：
名称：Mario Nawfal
推特用户名：@MarioNawfal
头像：https://pbs.twimg.com/profile_images/1670905743619268609/pYItlWat_normal.jpg
是否蓝V认证：是（blue_verified 为 True）
转发推文的互动数据：
点赞数：3821
回复数：303
转发数：553
引用数：26
浏览量：786964
4. 媒体信息                         （保留，如何下载？？）
媒体类型：图片
媒体列表：
图片1：
媒体URL：https://pbs.twimg.com/media/Gil1rmKWIAAtGPk.jpg
媒体ID：1885167310870028288
尺寸：宽 1116，高 559
图片2：
媒体URL：https://pbs.twimg.com/media/Gil14ofXYAEV3oc.jpg
媒体ID：1885167534833360897
尺寸：宽 900，高 600
总结
作者：Elon Musk（@elonmusk）
推文内容：转发了 @MarioNawfal 的推文，内容是关于特斯拉被评为2024年美国100家最佳雇主之一。
媒体：包含两张图片，分别是特斯拉的成就展示和相关数据图表。
如果你还有其他问题，或者需要进一步解析其他部分，请随时告诉我！




{'tweet_id': '1885214111140548664',
 'bookmarks': 1682,
 'created_at': 'Fri Jan 31 06:30:44 +0000 2025',
 'favorites': 5822,
 'text': 'Hmm',
 'lang': 'qst',
 'views': '2488457',
 'quotes': 62,
 'entities': {'hashtags': [],
  'symbols': [],
  'timestamps': [],
  'urls': [],
  'user_mentions': []},
 'replies': 1332,
 'retweets': 1041,
 'conversation_id': '1885214111140548664',
 'media': [],
 'author': {'rest_id': '44196397',
  'name': 'Elon Musk',
  'screen_name': 'elonmusk',
  'avatar': 'https://pbs.twimg.com/profile_images/1874558173962481664/8HSTqIlD_normal.jpg',
  'blue_verified': True},
 'quoted': {'tweet_id': '1885171399200833930',
  'bookmarks': 5048,
  'created_at': 'Fri Jan 31 03:41:01 +0000 2025',
  'favorites': 3675,
  'text': "Y Combinator JUST announced what startups they want to fund next in 2025. And it's mostly AI that replaces $100k/year job functions.\n\nMy notes below in case it's helpful to you: https://t.co/5I6fxzZiSv",
  'lang': 'en',
  'views': '2823386',
  'quotes': 139,
  'replies': 365,
  'retweets': 583,
  'conversation_id': '1885171399200833930',
  'author': {'rest_id': '14642331',
   'name': 'GREG ISENBERG',
   'screen_name': 'gregisenberg',
   'avatar': 'https://pbs.twimg.com/profile_images/1577116785656139776/5mi0qgTz_normal.jpg',
   'blue_verified': True},
  'media': {'photo': [{'media_url_https': 'https://pbs.twimg.com/media/Gil4CQpXEAAsb8h.jpg',
     'id': '1885169899254779904',
     'sizes': {'h': 1200, 'w': 934}}]}}} 
马斯克自己的推文内容是Hmm，引用quote了一篇gregisenberg的推文，该推文还包含meida