import json

with open('video_src.json', 'r') as video:
	videos = json.loads(video.read())
	markdown = ''
	for video_key in videos:
		name = f'Name - {video_key}:'

		if isinstance(videos[video_key], dict):
			link = videos[video_key]['link']
			video_src = videos[video_key]['video_src']
		elif isinstance(videos[video_key], str):
			link = videos[video_key]
			video_src = ''

		hh3d_link = f'[HH3D_Link]({link})' if len(link) != 0 else ''
		hh3d_video_src = f'[HH3D_Source]({video_src})' if len(video_src) != 0 else ''

		if 'blob' in video_src:
			hh3d_video_src = f'**BLOB_LINK** {hh3d_video_src}'			

		markdown += f"<hr>\n\n### {name}\n\n{hh3d_link}\n\n{hh3d_video_src}\n\n<hr>\n<br> "
	with open('link.md', 'w') as linkmd:
		linkmd.write(markdown)
		