import { Line } from 'react-chartjs-2';

const GraphWithIsbn = ({ _array }) => {
  const sortedArray = _array.sort((a, b) => {
    let x = a.crawl_date.toLowerCase();
    let y = b.crawl_date.toLowerCase();
    if (x < y) {
      return -1;
    }
    if (x > y) {
      return 1;
    }
    return 0;
  });

  const title = sortedArray[0].book.title;
  const labels = sortedArray.map((data) => {
    return data.crawl_date.slice(0, 10);
  });

  let assumeMaxRank = Math.max(
    ...sortedArray.map((data) => {
      return data.rank;
    }),
  );

  if (assumeMaxRank % 10 === assumeMaxRank) assumeMaxRank = 10;
  else if (assumeMaxRank % 100 === assumeMaxRank) assumeMaxRank = 100;

  const datasets = [
    {
      label: '순위',
      data: sortedArray.map((data) => {
        return data.rank;
      }),
      fill: false,
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgba(255, 99, 132, 0.2)',
      yAxisID: 'y1',
    },
    {
      label: '판매지수',
      data: sortedArray.map((data) => {
        return data.sales_point;
      }),
      fill: false,
      backgroundColor: 'rgb(65,105,225)',
      borderColor: 'rgba(65,105,225, 0.2)',
      yAxisID: 'y2',
    },
  ];

  const graphData = { labels: labels, datasets: datasets };

  const options = {
    plugins: {
      title: {
          display: true,
          text: title
      }
    },
    scales: {
      y1: {
        suggestedMin: 1,
        suggestedMax: assumeMaxRank,
        type: 'linear',
        display: true,
        position: 'left',
        reverse: true,
        ticks: {
          stepSize: 1,
        },
      },
      y2: {
        type: 'linear',
        display: true,
        position: 'right',
        grid: {
          drawOnChartArea: false,
        },
      },
    },
  };

  return (
    <>
      <Line data={graphData} options={options} />
    </>
  );
};

export default GraphWithIsbn;
