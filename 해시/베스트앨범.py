from collections import defaultdict

def solution(genres, plays):
    answer = []
    album_dict = defaultdict(list)
    play_count = defaultdict(int)
    for i in range(len(genres)):
        album_dict[genres[i]].append((plays[i], i))
        play_count[genres[i]] += plays[i]
    count_list = sorted(play_count.items(), key=lambda x: x[1], reverse=True)

    for key in album_dict.keys():
        album_dict[key].sort(reverse=True, key=lambda x: (x[0], -x[1]))

    for album, total in count_list:
        if len(album_dict[album]) >= 2:
            answer.append(album_dict[album][0][1])
            answer.append(album_dict[album][1][1])
        else:
            answer.append(album_dict[album][0][1])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
