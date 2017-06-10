from pymediainfo import MediaInfo
media_info = MediaInfo.parse('test.mp4')
for track in media_info.tracks:
    print(track)
    if track.track_type == 'Video':
        print(track.format)
        print(track.format_info)
        print(track.format_profile)
        print(track.format_settings)
        print(track.codec_id)
        print(track.duration)
        print(track.nominal_bit_rate)
        print(track.width)
        print(track.height)
        print(track.display_aspect_ratio)
        print(track.frame_rate_mode)
        print(track.frame_rate)
        print(track.color_space)
        print(track.chroma_subsampling)
        print(track.bit_depth)
        print(track.scan_type)
        print(track.language)




