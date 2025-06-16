
module my_module_tb;
    logic clk = 0, rst = 0, start = 0;
    logic [7:0] in_data, in_index, out_data;
    logic done;

    logic [7:0] features [0:135];
    logic [7:0] golden_out;

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
        $readmemh("mem_files/features.mem", features);
        $readmemh("mem_files/golden.mem", golden_out);
    end

    initial begin
        $display("=== Testbench Start ===");
        rst = 1; #20; rst = 0;

        for (int i = 0; i < 136; i++) begin
            in_index = i;
            in_data  = features[i];
            #10;
        end

        start = 1; #10; start = 0;
        wait (done == 1);

        $display("HW Output    : %0x", out_data);
        $display("Golden Output: %0x", golden_out);

        if (out_data === golden_out)
            $display("PASS: Hardware matches software.");
        else
            $display("FAIL: Mismatch detected.");

        $finish;
    end
endmodule
