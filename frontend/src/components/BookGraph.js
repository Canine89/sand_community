import { Line } from 'react-chartjs-2';

const BookGraph = ({ renderingData }) => {
  // console.log(renderingData);
  const rank = renderingData.map((data) => {
    return data.rank;
  });
  const title = renderingData.map((data) => {
    return data.title;
  });
  const datasets = [
    {
      label: 'rank',
      data: rank,
      fill: false,
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgba(255, 99, 132, 0.2)',
    },
  ];
  const graphData = { labels: title, datasets: datasets };
  const options = {
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
            reverse: true,
          },
        },
      ],
    },
  };
  return (
    <div>
      <Line data={graphData} options={options} />
    </div>
  );
};

export default BookGraph;
