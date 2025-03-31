import axios from "axios";
import { useEffect, useMemo, useRef, useState } from "react";
import { usePagination, useSortBy, useTable } from "react-table";

// Translation table as provided
const translation_table = {
  0: [['I', 0.42308274], ['lot', 0.06674201], ['day', 0.039722823], ['great', 0.032242015], ['interested', 0.022836346], ['work', 0.0169033], ['right', 0.015190968], ['idea', 0.010739183], ['little', 0.009951335], ['talk', 0.009923141]],
  1: [['god', 0.1131398], ['religion', 0.04660084], ['human', 0.02918333], ['believe', 0.023585899], ['worship', 0.017102381], ['religious', 0.014414554], ['belief', 0.013147227], ['deity', 0.01309805], ['create', 0.012831582], ['sacrifice', 0.012508558]],
  2: [['language', 0.124512], ['write', 0.08139583], ['word', 0.039391853], ['use', 0.03507263], ['character', 0.030553468], ['script', 0.02473739], ['speak', 0.022323893], ['sumerian', 0.021822676], ['cuneiform', 0.017732823], ['chinese', 0.01619075]],
  3: [['ancient', 0.33579928], ['egyptian', 0.09181423], ['greek', 0.088625886], ['egypt', 0.08286653], ['greece', 0.032000802], ['roman', 0.021750648], ['modern', 0.02076619], ['ancient egypt', 0.016951146], ['culture', 0.016848402], ['romans', 0.016652746]],
  4: [['civilization', 0.22312757], ['culture', 0.05062111], ['bce', 0.036451124], ['valley', 0.034371614], ['indus', 0.02758554], ['early', 0.025199411], ['write', 0.021735111], ['mesopotamia', 0.021447105], ['advance', 0.019490477], ['river', 0.017231654]],
  5: [['use', 0.0563587], ['earth', 0.03470323], ['planet', 0.019739857], ['sun', 0.017674744], ['day', 0.017168108], ['water', 0.01631455], ['star', 0.015677825], ['chariot', 0.012902217], ['sky', 0.01079269], ['invent', 0.010785279]],
  6: [['world', 0.12169692], ['century', 0.108570136], ['th', 0.08184704], ['music', 0.041416615], ['history', 0.023409933], ['british', 0.021847144], ['ad', 0.01997235], ['country', 0.019661047], ['th century', 0.016499516], ['million', 0.016357249]],
  7: [['mean', 0.023412807], ['way', 0.019665882], ['question', 0.017899886], ['answer', 0.016671369], ['different', 0.01465464], ['actually', 0.012993585], ['fact', 0.01209567], ['point', 0.0116960425], ['term', 0.011299607], ['example', 0.009960443]],
  8: [['black', 0.036708266], ['group', 0.03162274], ['african', 0.02502196], ['genetic', 0.020623008], ['arab', 0.020156674], ['origin', 0.017212244], ['ancestor', 0.017150054], ['descendant', 0.016790608], ['population', 0.016488235], ['africa', 0.016023692]],
  9: [['china', 0.19397524], ['chinese', 0.13013294], ['country', 0.03424035], ['japan', 0.02543835], ['korea', 0.02398201], ['korean', 0.023239017], ['japanese', 0.019378044], ['ancient china', 0.013100855], ['culture', 0.012763331], ['government', 0.011052909]],
  10: [['empire', 0.06546874], ['war', 0.03805445], ['great', 0.022420274], ['power', 0.02104357], ['conquer', 0.0198222], ['army', 0.018070927], ['state', 0.017638095], ['military', 0.016417196], ['kingdom', 0.013342539], ['land', 0.013074796]],
  11: [['dynasty', 0.10086495], ['chinese', 0.047330797], ['emperor', 0.0428284], ['china', 0.033864807], ['shang', 0.032038517], ['han', 0.025657922], ['history', 0.018659031], ['king', 0.017369345], ['tang', 0.014544328], ['bc', 0.013697426]],
  12: [['sumerian', 0.11267381], ['city', 0.0430531], ['king', 0.03798528], ['bc', 0.035386074], ['mesopotamia', 0.03012095], ['babylonian', 0.019049268], ['assyrian', 0.018817531], ['sumer', 0.016331721], ['akkadian', 0.014632638], ['mesopotamian', 0.014010754]],
  13: [['society', 0.025259892], ['social', 0.014842616], ['cultural', 0.013343246], ['culture', 0.01242214], ['influence', 0.012229899], ['development', 0.010800666], ['significant', 0.0102680875], ['political', 0.0100427745], ['trade', 0.00912144], ['include', 0.008728693]],
  14: [['india', 0.16702268], ['indian', 0.059587114], ['old', 0.05680315], ['tamil', 0.053449996], ['civilisation', 0.04655956], ['oldest', 0.039603204], ['pakistan', 0.029305102], ['sanskrit', 0.019986443], ['dravidian', 0.016920203], ['indians', 0.016850622]],
  15: [['site', 0.021212723], ['early', 0.019237736], ['stone', 0.014262768], ['evidence', 0.013549692], ['date', 0.012873712], ['use', 0.012729812], ['animal', 0.012223568], ['bc', 0.01068862], ['remain', 0.010414574], ['period', 0.009461466]],
  16: [['flood', 0.052936602], ['story', 0.050480407], ['book', 0.026421132], ['myth', 0.023368258], ['bible', 0.020064805], ['great', 0.017870435], ['record', 0.014559987], ['evidence', 0.014314353], ['water', 0.014232559], ['epic', 0.013208811]],
  17: [['man', 0.03118686], ['woman', 0.020668102], ['child', 0.01306244], ['son', 0.012024667], ['life', 0.011699837], ['family', 0.010383909], ['let', 0.008569136], ['father', 0.008346778], ['king', 0.008274249], ['die', 0.007460078]],
  18: [['year', 0.11390179], ['ago', 0.030773029], ['live', 0.02888506], ['age', 0.024064466], ['thousand', 0.021980243], ['human', 0.01949753], ['river', 0.01895415], ['long', 0.018707424], ['population', 0.015507748], ['start', 0.012671252]],
  19: [['east', 0.045709915], ['europe', 0.044841837], ['asia', 0.043829147], ['western', 0.041578252], ['european', 0.039705995], ['south', 0.033289667], ['west', 0.032468624], ['north', 0.028607909], ['middle', 0.025545558], ['america', 0.022146361]],
};

const ContentTableComponent = () => {
  const isFirstRender = useRef(true);
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [totalPages, setTotalPages] = useState(1);
  const [expandedCells, setExpandedCells] = useState({});
  const [isModalOpen, setIsModalOpen] = useState(false); // State for modal visibility

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get("http://localhost:8000/get_content?page=1");
        setData(response.data.data || []);
        setTotalPages(response.data.total_pages || 1);
      } catch (error) {
        console.error("Error fetching data:", error);
        setData([]);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, []);

  const columns = useMemo(
    () => [
      { Header: "Text", accessor: "text", sortType: "basic" },
      { Header: "Search Keyword", accessor: "search_keyword", sortType: "basic" },
      { Header: "Source", accessor: "source", sortType: "basic" },
      { Header: "Preprocessed Text", accessor: "preprocessed_text", sortType: "basic" },
      {
        Header: "Preprocessed Token",
        accessor: "preprocessed_token",
        disableSortBy: true,
        Cell: ({ value, row, column }) => {
          const key = `${row.index}-${column.id}`;
          const isExpanded = expandedCells[key];
          const maxTokensCollapsed = 3;
          const tokens = Array.isArray(value) ? value : [value];
          const displayedTokens = isExpanded ? tokens : tokens.slice(0, maxTokensCollapsed);
          const hasMore = !isExpanded && tokens.length > maxTokensCollapsed;

          return (
            <div className="flex flex-wrap gap-1">
              {displayedTokens.map((token, index) => (
                <span key={index} className="px-2 py-1 bg-indigo-600 text-white rounded-md text-xs whitespace-nowrap">
                  {token}
                </span>
              ))}
              {hasMore && <span className="px-2 py-1 text-gray-400 text-xs">...</span>}
            </div>
          );
        },
      },
      { Header: "Sentiment Label", accessor: "siebert_sentiment_label", sortType: "basic" },
      { Header: "Sentiment Score", accessor: "siebert_sentiment_score", sortType: "basic" },
      { Header: "Topics", accessor: "topics", disableSortBy: true },
    ],
    [expandedCells]
  );

  const toggleExpand = (rowIndex, columnId) => {
    setExpandedCells((prev) => {
      const key = `${rowIndex}-${columnId}`;
      return { ...prev, [key]: !prev[key] };
    });
  };

  const {
    getTableProps,
    getTableBodyProps,
    headerGroups,
    page: tablePage,
    prepareRow,
    canPreviousPage,
    canNextPage,
    nextPage,
    previousPage,
    state: { pageIndex, sortBy },
  } = useTable(
    {
      columns,
      data,
      initialState: { pageIndex: 0, pageSize: 10 },
      manualPagination: true,
      manualSortBy: true,
      pageCount: totalPages,
    },
    useSortBy,
    usePagination
  );

  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }
    const fetchData = async () => {
      setLoading(true);
      try {
        const sortParam = sortBy.length > 0 ? `&sortBy=${sortBy[0].id}&order=${sortBy[0].desc ? "desc" : "asc"}` : "";
        const response = await axios.get(`http://localhost:8000/get_content?page=${pageIndex + 1}${sortParam}`);
        setData(response.data.data || []);
        setTotalPages(response.data.total_pages || 1);
      } catch (error) {
        console.error("Error fetching data:", error);
        setData([]);
      } finally {
        setLoading(false);
      }
    };
    fetchData();
  }, [pageIndex, sortBy]);

  if (loading) return <p className="text-white text-lg">Loading...</p>;

  return (
    <div className="p-4 bg-gray-900">
      {/* Button to Open Modal */}
      <div className="mb-6">
        <button
          onClick={() => setIsModalOpen(true)}
          className="px-4 py-2 bg-indigo-600 text-white rounded hover:bg-indigo-500"
        >
          View Topic Modeling Visualization
        </button>
      </div>

      {/* Main Content Table */}
      <table {...getTableProps()} className="w-full border border-gray-700 shadow-md rounded-lg bg-gray-800">
        <thead className="bg-gray-700">
          {headerGroups.map((headerGroup) => (
            <tr {...headerGroup.getHeaderGroupProps()}>
              {headerGroup.headers.map((column) => (
                <th
                  {...column.getHeaderProps(column.getSortByToggleProps())}
                  className={`p-3 text-left border border-gray-600 font-semibold text-white ${
                    column.canSort ? "cursor-pointer hover:bg-gray-600" : ""
                  }`}
                >
                  <div className="flex items-center">
                    {column.render("Header")}
                    {column.canSort && (
                      <span className="ml-2">
                        {column.isSorted ? (column.isSortedDesc ? "↓" : "↑") : "↕"}
                      </span>
                    )}
                  </div>
                </th>
              ))}
            </tr>
          ))}
        </thead>
        <tbody {...getTableBodyProps()}>
          {tablePage.map((row, rowIndex) => {
            prepareRow(row);
            return (
              <tr {...row.getRowProps()} className="hover:bg-gray-600">
                {row.cells.map((cell) => {
                  const key = `${rowIndex}-${cell.column.id}`;
                  const isExpanded = expandedCells[key];
                  return (
                    <td
                      {...cell.getCellProps()}
                      className={`p-3 border border-gray-700 cursor-pointer transition-all duration-200 text-white ${
                        isExpanded ? "whitespace-normal" : "truncate overflow-hidden max-w-xs"
                      }`}
                      onDoubleClick={() => toggleExpand(rowIndex, cell.column.id)}
                    >
                      <div
                        className={
                          isExpanded
                            ? "absolute bg-gray-800 p-2 shadow-lg border border-gray-700 rounded-md z-10 text-white"
                            : "truncate overflow-hidden max-w-xs"
                        }
                      >
                        {cell.render("Cell")}
                      </div>
                    </td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>

      {/* Pagination Controls */}
      <div className="flex justify-between items-center mt-4 text-white">
        <button
          onClick={previousPage}
          disabled={!canPreviousPage}
          className="px-4 py-2 bg-gray-700 text-white rounded hover:bg-gray-600 disabled:opacity-50"
        >
          Previous
        </button>
        <span>Page {pageIndex + 1} of {totalPages}</span>
        <button
          onClick={nextPage}
          disabled={!canNextPage}
          className="px-4 py-2 bg-gray-700 text-white rounded hover:bg-gray-600 disabled:opacity-50"
        >
          Next
        </button>
      </div>

      {/* Translation Table */}
      <div className="mt-8">
        <h2 className="text-xl font-semibold text-white mb-4">Topic Translation Table</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {Object.entries(translation_table).map(([topicNum, words]) => (
            <div key={topicNum} className="bg-gray-800 p-4 rounded-lg shadow-md">
              <h3 className="text-lg font-medium text-white">Topic {topicNum}</h3>
              <ul className="mt-2">
                {words.map(([word, prob], index) => (
                  <li key={index} className="text-sm text-gray-300">
                    {word}: {(prob * 100).toFixed(2)}%
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>

      {/* Modal for Topic Modeling Visualization */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-gray-900 bg-opacity-75 flex items-center justify-center z-50">
          <div className="bg-gray-800 rounded-lg shadow-lg w-11/12 md:w-3/4 lg:w-2/3 max-h-[90vh] overflow-auto">
            <div className="p-4 border-b border-gray-700 flex justify-between items-center">
              <h2 className="text-xl font-semibold text-white">Topic Modeling Visualization</h2>
              <button
                onClick={() => setIsModalOpen(false)}
                className="text-gray-400 hover:text-white focus:outline-none"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12"></path>
                </svg>
              </button>
            </div>
            <div className="p-4">
              <iframe
                src="http://localhost:8000/static/lda_visualization.html"
                width="100%"
                height="800px"
                className="border-0"
                title="LDA Visualization"
              />
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ContentTableComponent;