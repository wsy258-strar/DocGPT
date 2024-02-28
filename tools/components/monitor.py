import datetime

def community_tokens_available_pct(used):
	# used = used
	print("used:",used)
	limit = 100000
	pct = (100.0 * (limit-used) / limit) if limit else 0
	pct = max(0, pct)
	pct = min(100, pct)
	print(pct)
	return pct


def community_tokens_refresh_in():
	x = datetime.datetime.now()
	print("now timw:",x)
	dt = (x.replace(hour=23, minute=59, second=59) - x).seconds
	h = dt // 3600
	m = dt  % 3600 // 60
	return f"{h} h {m} min"