module my_module_tb;
    logic clk = 0, rst = 0, start = 0;
    logic [7:0] in_data, in_index, out_data;
    logic done;

    logic [7:0] features [0:135];

    my_module dut (
        .clk(clk),
        .rst(rst),
        .start(start),
        .in_data(in_data),
        .in_index(in_index),
        .out_data(out_data),
        .done(done)
    );

    always #5 clk = ~clk;

    initial begin
        // Initialize all features with constant
        for (int j = 0; j < 136; j++) begin
            features[j] = 8'h7f;
        end

        rst = 1; #10; rst = 0;

        for (int t = 0; t < 1; t++) begin
            // Feed all features
            for (int i = 0; i < 136; i++) begin
                @(posedge clk);
                in_index = i;
                in_data = features[i];
                start = 1;
                @(posedge clk);
                start = 0;
            end

            // Wait for computation to complete
            wait (done == 1);

            // Dump final output
            $display("Final HW Output (out_data) = %0h", out_data);
        end

        $finish;
    end
endmodule
