usage='bash module.sh [filename]'
if [ $# -lt 1 ]
then
  echo 'Too few arguments'
  printf "\nUsage:\n\n$usage\n"
  exit 1
elif [ $# -gt 1 ]
then
  echo 'Too many arguments'
  printf "\nUsage:\n\n$usage\n"
  exit 1
fi

file=`grep '==' $1`
count=`grep '==' $1 | wc -l`

echo Starting Installation
printf "\n********\n\n"
for i in `seq 1 $count`
do
  line=`echo $file | cut -d ',' -f $i`

  name=`echo $line | cut -d '=' -f1`
  version=`echo $line | cut -d '=' -f3`

  echo Installing $name $version...

  command pip install $name
  if [ $? -eq 0 ]
  then
    echo Success!
  else
    echo FAILED! Found no module named $name and version $version
  fi
  printf "\n********\n\n"
done
