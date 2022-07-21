            int _min, _sec = 0;
            string tmpString = _data[data_index];
            tie(_min, _sec) = converToInt(tmpString);
            cout << "conversion done!" << endl;
            
            cout << "_min : " << _min << " _sec : " << _sec << endl;


            if(curr_min == _min && curr_sec == _sec){
                data_index += 1;

                if(_map.find(tmpString) != _map.end()){
                    string tmpTeam = _map[tmpString];
                    if(tmpTeam == "1") score1 += 1;
                    else if(tmpTeam == "2") score2 += 1;
                }

            }