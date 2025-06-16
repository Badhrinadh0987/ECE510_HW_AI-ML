module drowsiness_feature_memory #(
    parameter FEATURE_WIDTH = 8,
    parameter FEATURE_COUNT = 136,
    parameter SAMPLE_COUNT = 10
)(
    input  logic [$clog2(SAMPLE_COUNT)-1:0] sample_index, // sample selector (0 to SAMPLE_COUNT-1)
    output logic [FEATURE_WIDTH-1:0] sample_data [0:FEATURE_COUNT-1] // 136-D sample output
);

    // Flat memory to hold all features: SAMPLE_COUNT * FEATURE_COUNT
    logic [FEATURE_WIDTH-1:0] memory_array [0:(FEATURE_COUNT * SAMPLE_COUNT) - 1];

    // Load memory from .mem file
    initial begin
        $display("Loading features from landmark_features.mem...");
        $readmemh("landmark_features.mem", memory_array);
        $display("Done loading features.");
    end

    // Combinational logic to extract a sample block
    always_comb begin
        for (int i = 0; i < FEATURE_COUNT; i++) begin
            sample_data[i] = memory_array[sample_index * FEATURE_COUNT + i];
        end
    end

endmodule
