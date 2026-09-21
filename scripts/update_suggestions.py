import os,json,urllib.parse,urllib.request,datetime,re
KEY=os.environ.get("TMDB_API_KEY")
if not KEY: raise SystemExit("GitHub secret TMDB_API_KEY fehlt")
with open("movies.json",encoding="utf-8") as f: existing=json.load(f).get("movies",[])
norm=lambda s:re.sub(r"[^a-z0-9]+","",str(s).lower())
known={norm(x.get("title","")) for x in existing}
genre_names={28:"Action",18:"Drama",53:"Thriller",80:"Krimi",9648:"Mystery",27:"Horror",878:"Science-Fiction"}
found=[]
for page in (1,2,3):
 p={"api_key":KEY,"language":"de-DE","sort_by":"vote_average.desc","vote_count.gte":250,
    "vote_average.gte":6.5,"with_genres":"28|18|53|80|9648|27|878","include_adult":"false","page":page}
 u="https://api.themoviedb.org/3/discover/movie?"+urllib.parse.urlencode(p)
 with urllib.request.urlopen(u,timeout=30) as r:data=json.load(r)
 for x in data.get("results",[]):
  title=x.get("title") or x.get("original_title") or ""
  if not title or norm(title) in known: continue
  found.append({"id":"tmdb-"+str(x["id"]),"title":title,"year":(x.get("release_date") or "")[:4],
   "genres":[genre_names[g] for g in x.get("genre_ids",[]) if g in genre_names],
   "description":x.get("overview") or "","rating":x.get("vote_average"),"source":"TMDB"})
  known.add(norm(title))
  if len(found)>=20:break
 if len(found)>=20:break
with open("suggestions.json","w",encoding="utf-8") as f:
 json.dump({"updated":datetime.datetime.now(datetime.timezone.utc).isoformat(),"movies":found},f,ensure_ascii=False,indent=2)
