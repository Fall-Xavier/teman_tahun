import sys, requests, json
ses=requests.Session()
id = []
token = "EAAGNO4a7r2wBABheSn8urqtgMKnQt7XjRDE23wzZBwCdohKiwUbZA5zoXBI9teZB65GYpuIGKCU8JCNx9jOspx15tcLAPjWN2CYuIjtOS8ZBiB1keZCLxhLWtoZAB6ZAbLZBIeDH1I5uM2P1hVY8E02fw6ZA13HGPC5J4HgH6xdxJ9CYnbXJkS6m4G1p4LZBQxe4EZD"
cok = "datr=UvhMY9H1yIPIvN0sz2XfKIgH;sb=UvhMYwKwS7tV2nFKzuHxSSc_;locale=id_ID;wd=360x627;c_user=100086710907138;xs=12:fryLyvk9zcPltg:2:1666062926:-1:-1;m_page_voice=100086710907138;zsh=ASQ2F66Vq1vUYH9THvdu1OI19MozdRS29I1Qshnmk3Le-smJwN5Y56gzwTEqtfq_nBM03M2G_z6gTcMHYVbzHj5xWwHfAR-7XR5d8hRi4rTH1oEfdKwj1IrtZ4Sk_Hig8g1X1pnbn4bvsdBJS26qjyf0tHviqAmjNj7aIezP3rpuHATzKVThwm9VA89cGEVHvFW6GDc-OXfFGRFWymAjghFLNVHF2-z-k28nPmkWTSmSXns_K1OhqQhT3VQ288MNqmGDjOfxfmAJW9O6J0KE5gXUUjco98BsHNrf8V7nmL-5UvQNvCTlIK410tQvGGNxldxX;fr=0EmVjyNFtFbOH7oWe.AWWks-yjJPpnaQOTZPaEC4Qw-7s.BjTPhS.PD.AAA.0.0.BjUjIx.AWWm5HgX03k;"
cookie = {"cookie":cok}

idt = input("masukan id : ")
ask = input("masukan tahun : ").split(",")
try:
	url = ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie)
	jason = json.loads(url.text)
	for i in jason["friends"]["data"]:
		if "2022" in ask:
			if i["id"][:5] in ["10008"]:
				print(i["id"]+"<=>"+i["name"])
		if "2021" in ask:
			if i["id"][:5] in ["10008"] or i["id"][:5] in ["10007"] or i["id"][:5] in ["10006"]:
				print(i["id"]+"<=>"+i["name"])
		if "2020" in ask:
			if i["id"][:5] in ["10005"]:
				print(i["id"]+"<=>"+i["name"])
		if "2019" in ask or "2020" in ask:
			if i["id"][:5] in ["10004"] or i["id"][:5] in ["10003"]:
				print(i["id"]+"<=>"+i["name"])
		if "2018" in ask or "2019" in ask:
			if i["id"][:5] in ["10003"]:
				print(i["id"]+"<=>"+i["name"])
		if "2016" in ask or "2017" in ask:
			if i["id"][:5] in ["10002"]:
				print(i["id"]+"<=>"+i["name"])
		if "2015" in ask or "2016" in ask:
			if i["id"][:5] in ["10001"]:
				print(i["id"]+"<=>"+i["name"])
		if "2015" in ask:
			if i["id"][:6] in ["100009"]:
				print(i["id"]+"<=>"+i["name"])
		if "2014" in ask or "2015" in ask:
			if i["id"][:6] in ["100007"] or i["id"][:6] in ["100008"]:
				print(i["id"]+"<=>"+i["name"])
		if "2013" in ask or "2014" in ask:
			if i["id"][:6] in ["100005"] or i["id"][:6] in ["100006"]:
				print(i["id"]+"<=>"+i["name"])
		if "2012" in ask or "2013" in ask:
			if i["id"][:6] in ["100004"]:
				print(i["id"]+"<=>"+i["name"])
		if "2011" in ask or "2012" in ask:
			if i["id"][:6] in ["100002"] or i["id"][:6] in ["100003"]:
				print(i["id"]+"<=>"+i["name"])
		if "2010" in ask or "2011" in ask:
			if i["id"][:6] in ["100001"]:
				print(i["id"]+"<=>"+i["name"])
		if "2010" in ask:
			if i["id"][:7] in ["1000006"] or i["id"][:7] in ["1000007"] or i["id"][:7] in ["1000008"] or i["id"][:7] in ["1000009"]:
				print(i["id"]+"<=>"+i["name"])
		if "2009" in ask:
			if i["id"][:7] in ["1000000"] or i["id"][:7] in ["1000001"] or i["id"][:7] in ["1000002"] or i["id"][:7] in ["1000003"] or i["id"][:7] in ["1000004"] or i["id"][:7] in ["1000005"]:
				print(i["id"]+"<=>"+i["name"])
		if "2009" in ask:
			if i["id"][:8] in ["10000000"] or i["id"][:9] in ["100000000"] or i["id"][:10] in ["1000000000"]:
				print(i["id"]+"<=>"+i["name"])
		if "2008" in ask or "2009" in ask:
			if len(i["id"]) in [9,10]:
				print(i["id"]+"<=>"+i["name"])
		if "2007" in ask or "2009" in ask:
			if len(i["id"]) in [8]:
				print(i["id"]+"<=>"+i["name"])
		if "2006" in ask or "2007" in ask:
			if len(i["id"]) in [7]:
				print(i["id"]+"<=>"+i["name"])
except Exception as e:
	print(e)