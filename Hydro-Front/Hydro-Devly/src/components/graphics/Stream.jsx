import { ResponsiveStream } from "@nivo/stream";

export const MyResponsiveStream = ({
    data = [
      {
        Raoul: 18,
        Josiane: 200,
        Marcel: 118,
        René: 143,
        Paul: 37,
        Jacques: 33,
      },
      {
        Raoul: 15,
        Josiane: 50,
        Marcel: 35,
        René: 188,
        Paul: 82,
        Jacques: 52,
      },
      {
        Raoul: 105,
        Josiane: 96,
        Marcel: 158,
        René: 117,
        Paul: 125,
        Jacques: 81,
      },
      {
        Raoul: 129,
        Josiane: 11,
        Marcel: 69,
        René: 42,
        Paul: 76,
        Jacques: 99,
      },
      {
        Raoul: 31,
        Josiane: 172,
        Marcel: 175,
        René: 110,
        Paul: 10,
        Jacques: 57,
      },
      {
        Raoul: 87,
        Josiane: 91,
        Marcel: 196,
        René: 152,
        Paul: 17,
        Jacques: 36,
      },
      {
        Raoul: 58,
        Josiane: 157,
        Marcel: 149,
        René: 51,
        Paul: 10,
        Jacques: 92,
      },
      {
        Raoul: 46,
        Josiane: 141,
        Marcel: 185,
        René: 187,
        Paul: 179,
        Jacques: 81,
      },
      {
        Raoul: 137,
        Josiane: 138,
        Marcel: 101,
        René: 152,
        Paul: 196,
        Jacques: 78,
      },
    ],
  }) => (
    <ResponsiveStream
      data={data}
      keys={["Raoul", "Josiane", "Marcel", "René", "Paul", "Jacques"]}
      margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
      axisTop={null}
      axisRight={null}
      axisBottom={{
        orient: "bottom",
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "",
        legendOffset: 36,
      }}
      axisLeft={{
        orient: "left",
        tickSize: 5,
        tickPadding: 5,
        tickRotation: 0,
        legend: "",
        legendOffset: -40,
      }}
      enableGridX={true}
      enableGridY={false}
      curve="linear"
      offsetType="none"
      order="insideOut"
      colors={{ scheme: "nivo" }}
      borderColor={{ from: "color", modifiers: [] }}
      defs={[
        {
          id: "dots",
          type: "patternDots",
          background: "inherit",
          color: "#2c998f",
          size: 4,
          padding: 2,
          stagger: true,
        },
        {
          id: "squares",
          type: "patternSquares",
          background: "inherit",
          color: "#e4c912",
          size: 6,
          padding: 2,
          stagger: true,
        },
      ]}
      fill={[
        {
          match: {
            id: "Paul",
          },
          id: "dots",
        },
        {
          match: {
            id: "Marcel",
          },
          id: "squares",
        },
      ]}
      dotSize={8}
      dotColor={{ from: "color" }}
      dotBorderWidth={2}
      dotBorderColor={{
        from: "color",
        modifiers: [["darker", 0.7]],
      }}
      legends={[
        {
          anchor: "bottom-right",
          direction: "column",
          translateX: 100,
          itemWidth: 80,
          itemHeight: 20,
          itemTextColor: "#999999",
          symbolSize: 12,
          symbolShape: "circle",
          effects: [
            {
              on: "hover",
              style: {
                itemTextColor: "#000000",
              },
            },
          ],
        },
      ]}
    />
  );