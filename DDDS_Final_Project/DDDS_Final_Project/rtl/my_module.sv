module my_module (
    input logic clk,
    input logic rst,
    input logic start,
    input logic [7:0] in_data,
    input logic [7:0] in_index,
    output logic [7:0] out_data,
    output logic done
);

    parameter FEATURE_COUNT = 136;

    logic [7:0] input_vector [0:FEATURE_COUNT-1];
    logic signed [7:0] weights [0:FEATURE_COUNT-1];

    logic signed [15:0] acc;
    logic [7:0] i;
    logic computing;

    initial $readmemh("mem_files/weights.mem", weights);

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            i <= 0;
            acc <= 0;
            done <= 0;
            computing <= 0;
            out_data <= 0;
        end else begin
            if (start && !computing) begin
                input_vector[in_index] <= in_data;
                if (in_index == FEATURE_COUNT-1) begin
                    i <= 0;
                    acc <= 0;
                    done <= 0;
                    computing <= 1;
                end
            end else if (computing) begin
                acc <= acc + $signed(input_vector[i]) * $signed(weights[i]);
                out_data <= acc[7:0];  // Output after every accumulation
                $display("ACC = %0h | OUT_DATA = %0h", acc, acc[7:0]);
                i <= i + 1;
                if (i == FEATURE_COUNT-1) begin
                    computing <= 0;
                    done <= 1;
                end
            end else begin
                done <= 0;
            end
        end
    end
endmodule