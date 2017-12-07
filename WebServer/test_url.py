query = "bannana"
string_query = "q=%s&lang=en&locale=us&count=100" % query
print(string_query)
at = "%40"
hashtag = "%23"
query2 = at+query
query3 = hashtag+query
string_query = "q=%s&lang=en&locale=us&count=100" % query2
print(string_query)
string_query = "q=%s&lang=en&locale=us&count=100" % query3
print(string_query)
