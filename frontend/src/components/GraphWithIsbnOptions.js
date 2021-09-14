import { Line } from 'react-chartjs-2';

const GraphWithIsbnOptions = ({ isbnData, title }) => {
  const labels = isbnData.map((data) => {
    return data.crawl_date.slice(0, 10);
  });

  const datasets = [
    {
      label: '순위',
      data: isbnData.map((data) => {
        return data.rank;
      }),
      fill: false,
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgba(255, 99, 132, 0.2)',
      yAxisID: 'y1',
    },
    {
      label: '판매지수',
      data: isbnData.map((data) => {
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
    scales: {
      y1: {
        suggestedMin: 1,
        suggestedMax: 600,
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
      <div className="text-gray-400 text-sm text-center">{title}</div>
      <Line data={graphData} options={options} />
    </>
  );
};

export default GraphWithIsbnOptions;
