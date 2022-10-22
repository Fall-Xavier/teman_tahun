import sys, requests, json
ses=requests.Session()
id = []
token = "EAAGNO4a7r2wBAJUEiImtEZCl7ghr3YeygSkUBuQfYlTM2E9izArKa0gRM8sPqeRBVMFd8XK1pOpX4ApwW2fJSHWiB2ZBSObVPe9ge5Wph6XDF7gdEH1g4ZA7LvJfWHTfkD67kZAxVRHFQz1iUlgM6ZALs3RsPWb4QbeZC9PHMvXmS4TnMODMA4"
cok = "datr=iNCjYmmHhYuMv0ThY-ziX4ne; sb=iNCjYiT79wzZTO6f94wl7kl5; locale=id_ID; zsh=ASSpeLi8usC44L-WCkIQNY5SeUzWbziBcAiS-rvbfoAVURfU77ZJhmo3F-1K-OjK0OtYnTphuUM0DOaWFfooguEv9mBXhNoF8TeSCMXMYllZTslIzRDfMduNhr5o37c-C6v7Wx-lEovSSD-KioErmTMtpuCJLXGmEII_iZZQHTVezGglANX8TavaaM-uGSRE5PyWVkWZ0HmSj5dXGJ1PtkR7LMet1mt7lCc1KcJytySs8CWWgwIX3_rUNKjrSiOqDiNorul8KUVyjQhSR5GHWvSaDf1Ae_aCIs8EkR0egXzXJkusi0gmRP3_KjddjRv31FHIHd8; m_pixel_ratio=3; fr=0dWHGzLagbRQlGPii.AWUotAJMJ8ptyvVO7fE4fXGGNLg.Bio9CI.Zj.AAA.0.0.BjU34i.AWV9hIN8YWA; c_user=100054965853953; xs=33:TADbglT-8TKixw:2:1666416162:-1:15948; m_page_voice=100054965853953; wd=360x648"
cookie = {"cookie":cok}

def getUID():
	idt = input(" masukan id : ")
	try:
		url = ses.get(f"https://graph.facebook.com/{idt}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}",cookies=cookie)
		jason = json.loads(url.text)
		for i in jason["friends"]["data"]:
			id.append(i["id"]+"<=>"+i["name"])
	except Exception as e:
		print(e)
		exit(" error kemungkinan tumbal mati atau target tidak bisa di dump")
	print(f" berhasil mengumpulkan {len(id)} id")
	tahun = input(" masukan tahun : ").split(",")
	for data in id:
		uid = data.split("<=>")[0]
		nama = data.split("<=>")[1]
		getTAHUN(tahun,uid,nama)
		
def getTAHUN(tahun,uid,nama):
	if "2022" in tahun:
		if uid[:5] in ["10008"]:
			print(uid+"<=>"+nama)
	if "2021" in tahun:
		if uid[:5] in ["10008"] or uid[:5] in ["10007"] or uid[:5] in ["10006"]:
			print(uid+"<=>"+nama)
	if "2020" in tahun:
		if uid[:5] in ["10005"]:
			print(uid+"<=>"+nama)
	if "2019" in tahun or "2020" in tahun:
		if uid[:5] in ["10004"] or uid[:5] in ["10003"]:
			print(uid+"<=>"+nama)
	if "2018" in tahun or "2019" in tahun:
		if uid[:5] in ["10003"]:
			print(uid+"<=>"+nama)
	if "2016" in tahun or "2017" in tahun:
		if uid[:5] in ["10002"]:
			print(uid+"<=>"+nama)
	if "2015" in tahun or "2016" in tahun:
		if uid[:5] in ["10001"]:
			print(uid+"<=>"+nama)
	if "2015" in tahun:
		if uid[:6] in ["100009"]:
			print(uid+"<=>"+nama)
	if "2014" in tahun or "2015" in tahun:
		if uid[:6] in ["100007"] or uid[:6] in ["100008"]:
			print(uid+"<=>"+nama)
	if "2013" in tahun or "2014" in tahun:
		if uid[:6] in ["100005"] or uid[:6] in ["100006"]:
			print(uid+"<=>"+nama)
	if "2012" in tahun or "2013" in tahun:
		if uid[:6] in ["100004"]:
			print(uid+"<=>"+nama)
	if "2011" in tahun or "2012" in tahun:
		if uid[:6] in ["100002"] or uid[:6] in ["100003"]:
			print(uid+"<=>"+nama)
	if "2010" in tahun or "2011" in tahun:
		if uid[:6] in ["100001"]:
			print(uid+"<=>"+nama)
	if "2010" in tahun:
		if uid[:7] in ["1000006"] or uid[:7] in ["1000007"] or uid[:7] in ["1000008"] or uid[:7] in ["1000009"]:
			print(uid+"<=>"+nama)
	if "2009" in tahun:
		if uid[:7] in ["1000000"] or uid[:7] in ["1000001"] or uid[:7] in ["1000002"] or uid[:7] in ["1000003"] or uid[:7] in ["1000004"] or uid[:7] in ["1000005"]:
			print(uid+"<=>"+nama)
	if "2009" in tahun:
		if uid[:8] in ["10000000"] or uid[:9] in ["100000000"] or uid[:10] in ["1000000000"]:
			print(uid+"<=>"+nama)
	if "2008" in tahun or "2009" in tahun:
		if len(uid) in [9,10]:
			print(uid+"<=>"+nama)
	if "2007" in tahun or "2009" in tahun:
		if len(uid) in [8]:
			print(uid+"<=>"+nama)
	if "2006" in tahun or "2007" in tahun:
		if len(uid) in [7]:
			print(uid+"<=>"+nama)
		
getUID()