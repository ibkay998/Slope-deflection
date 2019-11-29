dataset = [
        [
            [
                {"span": 6, "magnitude": 10, "load_type": "get","position_of_span":1,"order":1},
                {"span": 6, "magnitude": 8, "load_type": "point","position_of_span":2,"order":2},
            ],
            [18, 14.4, 6, 6],
        ],
    ]
released = dataset[0][0]
    
value = [x.get("load_type",None) for x in released]
for i,j in enumerate(dataset):
    print(value[i])