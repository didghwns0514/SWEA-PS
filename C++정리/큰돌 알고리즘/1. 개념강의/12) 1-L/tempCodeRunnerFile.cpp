    sort(_data, _data + sizeof(_data));
    
    bool isIterationNeeded = true;
    for(int i=1; i < sizeof(_data)-1; i++){
        for(int j=i; j < sizeof(_data); j++){
            if(_data[i] > M/2) {break; isIterationNeeded = false;}
            if(_data[i] + _data[j] == M) answer += 1;

        }

        if(!isIterationNeeded) break;
    }