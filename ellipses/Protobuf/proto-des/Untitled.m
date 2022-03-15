fid = fopen('crc.txt', 'r');
tLines = fgets(fid);
 numCols = numel(strfind(tLines,',')) + 1;
 fclose(fid);